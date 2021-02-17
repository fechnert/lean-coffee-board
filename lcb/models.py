import uuid

from django.conf import settings
from django.db import models


class UUIDModel(models.Model):
    """Abstract class for models with an uuid as primary key"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class SortableBoardObject(models.Model):
    """Abstract class for models with a defined position / ordering in a given board"""

    position = models.PositiveSmallIntegerField(blank=True)

    def save(self, *args, **kwargs):
        if self._state.adding:
            import pudb; pu.db
            max_obj_pos = self.__class__.objects.filter(board=self.board).order_by('position').last()
            self.position = max_obj_pos.position + 1 if max_obj_pos else 1

        return super().save(*args, **kwargs)

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
    vote_limit = models.PositiveSmallIntegerField(default=3)
    think_time_limit = models.DurationField()
    discuss_time_limit = models.DurationField()

    def __str__(self):
        return str(self.id)


class Lane(UUIDModel, SortableBoardObject):
    """Lane for assigning Cards to different categories"""

    board = models.ForeignKey('Board', on_delete=models.CASCADE)

    title = models.CharField(max_length=512)

    class Meta:
        unique_together = ('board', 'position')

    def __str__(self):
        return self.title


class Card(UUIDModel, SortableBoardObject):
    """Card which is assigned to a board"""

    board = models.ForeignKey('Board', on_delete=models.CASCADE)
    lane = models.ForeignKey('Lane', on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cards_created")

    title = models.CharField(max_length=512)
    votes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cards_voted", blank=True)

    class Meta:
        unique_together = ('board', 'position')

    def __str__(self):
        return self.title
