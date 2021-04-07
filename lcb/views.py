from rest_framework import filters, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from django.conf import settings

from lcb import models
from lcb import serializers


class VersionView(APIView):

    def get(self, request):
        """Return the version of the current running app"""
        data = {"version": settings.VERSION}
        return Response(data, status.HTTP_200_OK)


class BoardViewSet(viewsets.ModelViewSet):

    queryset = models.Board.objects.all()
    serializer_class = serializers.BoardSerializer


class LaneViewSet(viewsets.ModelViewSet):

    queryset = models.Lane.objects.all()
    serializer_class = serializers.LaneSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['board']
    ordering_fields = ['position', 'type']
    ordering = ['-type', 'position']


class CardViewSet(viewsets.ModelViewSet):

    queryset = models.Card.objects.all()
    serializer_class = serializers.CardSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['board', 'lane', 'owner']
