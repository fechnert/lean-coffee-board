from rest_framework import serializers
from rest_framework.validators import ValidationError

from django.contrib.auth.models import User

from lcb import models


class LoginSerializer(serializers.Serializer):
    """Parse the name for the user to create"""

    name = serializers.CharField(max_length=255)
    color = serializers.CharField(max_length=7)


class UserSerializer(serializers.Serializer):
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

    owner = UserSerializer()
    member_count = serializers.SerializerMethodField(read_only=True)
    card_count = serializers.SerializerMethodField(read_only=True)

    def get_member_count(self, board):
        return board.members.count()

    def get_card_count(self, board):
        return board.cards.count()

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
            'member_count',
            'card_count',
        ]


class BoardDetailSerializer(serializers.ModelSerializer):

    owner = UserSerializer()
    members = UserSerializer(many=True, read_only=True)
    phases = serializers.SerializerMethodField(read_only=True)

    def get_phases(self, board):
        return [{'id': k, 'name': v} for k, v in board.Phases.choices]

    class Meta:
        model = models.Board
        fields = [
            'id',
            'owner',
            'created',
            'phase',
            'phases',
            'title',
            'vote_limit',
            'think_time_limit',
            'discuss_time_limit',
            'members',
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
    owner = UserSerializer()

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
