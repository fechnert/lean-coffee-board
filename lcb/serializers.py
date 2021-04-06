from rest_framework import serializers

from lcb import models


class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Board
        fields = [
            'id',
            'created',
            'phase',
            'title',
            'vote_limit',
            'think_time_limit',
            'discuss_time_limit',
        ]


class LaneSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Lane
        fields = [
            'id',
            'board',
            'position',
            'title',
        ]


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Card
        fields = [
            'id',
            'board',
            'lane',
            'position',
            'title',
            'votes',
        ]
