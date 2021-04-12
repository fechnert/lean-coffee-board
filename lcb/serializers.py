from rest_framework import serializers

from lcb import models


class BoardSerializer(serializers.ModelSerializer):

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
