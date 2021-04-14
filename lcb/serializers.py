from rest_framework import serializers
from rest_framework.validators import ValidationError

from django.contrib.auth.models import User

from lcb import models


class LoginSerializer(serializers.Serializer):
    """Parse the name for the user to create"""

    name = serializers.CharField(max_length=255)
    color = serializers.CharField(max_length=7)


class OwnerSerializer(serializers.Serializer):
    """Nested serializer for the owner relation"""

    id = serializers.UUIDField(source="username")
    name = serializers.CharField(source="first_name")
    color = serializers.CharField(source="last_name")

    def to_internal_value(self, data):
        if not isinstance(data, str):
            raise ValidationError("This value needs to be the owner ID")

        try:
            return User.objects.get(username=data)
        except User.DoesNotExist:
            raise ValidationError("This user does not exist!")


class BoardSerializer(serializers.ModelSerializer):

    owner = OwnerSerializer()

    class Meta:
        model = models.Board
        fields = [
            'id',
            'owner',
            'created',
            'phase',
            'title',
            'vote_limit',
            'think_time_limit',
            'discuss_time_limit',
        ]


class LaneSerializer(serializers.ModelSerializer):

    position = serializers.IntegerField(required=False)

    class Meta:
        model = models.Lane
        fields = [
            'id',
            'board',
            'position',
            'type',
            'title',
        ]


class CardSerializer(serializers.ModelSerializer):

    position = serializers.IntegerField(required=False)
    owner = OwnerSerializer()

    class Meta:
        model = models.Card
        fields = [
            'id',
            'owner',
            'board',
            'lane',
            'position',
            'title',
            'votes',
        ]
