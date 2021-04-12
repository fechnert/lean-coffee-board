import uuid

from django.conf import settings
from django.db import models, transaction


class UUIDModel(models.Model):
    """Abstract class for models with an uuid as primary key"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class SortableMixin(models.Model):
    """Abstract class for models with a defined position"""

    position = models.PositiveSmallIntegerField(blank=True)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.create()
        else:
            self.move()

        return super().save(*args, **kwargs)

    def get_sortable_queryset(self):
        """Called to get the queryset to sort for"""
        raise NotImplementedError()

    def create(self):
        """Called if a new element is created"""
        result = self.get_sortable_queryset().aggregate(models.Max('position'))
        max_pos = result.get('position__max')
        self.position = 0 if max_pos is None else max_pos + 1

    def move(self, qs=None, old_instance=None):
        """Called if an element needs to be moved"""
        qs = qs or self.get_sortable_queryset()
        old_instance = old_instance or self.__class__.objects.get(id=self.id)

        with transaction.atomic():
            if old_instance.position > self.position:
                qs.filter(
                    position__lt=old_instance.position,
                    position__gte=self.position,
                ).exclude(
                    id=self.id
                ).update(
                    position=models.F('position') + 1,
                )
            else:
                qs.filter(
                    position__lte=self.position,
                    position__gt=old_instance.position,
                ).exclude(
                    id=self.id
                ).update(
                    position=models.F('position') - 1,
                )

    class Meta:
        abstract = True


class Board(UUIDModel):
    """Container for multiple cards"""

    class Phases(models.TextChoices):
        THINK = 't', 'Think'
        EXPLAIN = 'e', 'Explain'
        VOTE = 'v', 'Vote'
        DISCUSS = 'd', 'Discuss'

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    phase = models.CharField(max_length=1, choices=Phases.choices, default=Phases.THINK)

    # board settings
    title = models.CharField(max_length=512)
    vote_limit = models.PositiveSmallIntegerField(default=3)
    think_time_limit = models.DurationField()
    discuss_time_limit = models.DurationField()

    def __str__(self):
        return self.title


class Lane(UUIDModel, SortableMixin):
    """Lane for assigning Cards to different categories"""

    class Types(models.TextChoices):
        GATHER = 'g', 'Gather'
        DISCUSS = 'd', 'Discuss'

    board = models.ForeignKey('Board', on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=Types.choices, default=Types.GATHER)

    title = models.CharField(max_length=512)

    def get_sortable_queryset(self):
        return Lane.objects.filter(board=self.board, type=self.Types.GATHER)

    # class Meta:
    #     unique_together = ('board', 'position')

    def __str__(self):
        return self.title


class Card(UUIDModel, SortableMixin):
    """Card which is assigned to a board"""

    board = models.ForeignKey('Board', on_delete=models.CASCADE)
    lane = models.ForeignKey('Lane', on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cards_created")

    title = models.CharField(max_length=512)
    votes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cards_voted", blank=True)

    def get_sortable_queryset(self):
        return Card.objects.filter(lane=self.lane)

    def move(self, *args, **kwargs):
        qs = self.get_sortable_queryset()
        old_instance = self.__class__.objects.get(id=self.id)

        with transaction.atomic():

            # its possible to move cards to another lane
            if old_instance.lane != self.lane:

                # move cards of old lane one position back to fill the gap
                Card.objects.filter(
                    lane=old_instance.lane,
                    position__gt=old_instance.position,
                ).exclude(
                    id=self.id
                ).update(
                    position=models.F('position') - 1,
                )

                # move cards of new lane one position forward to create a gap
                qs.filter(
                    position__gte=self.position,
                ).update(
                    position=models.F('position') + 1,
                )

            else:
                super().move(qs, old_instance)

    # class Meta:
    #     unique_together = ('lane', 'position')

    def __str__(self):
        return self.title
