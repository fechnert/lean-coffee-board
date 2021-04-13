import uuid
import random
import string

from rest_framework import filters, status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from django_filters.rest_framework import DjangoFilterBackend

from django.conf import settings
from django.contrib.auth.models import User

from lcb import models, serializers, throttles


class VersionView(APIView):

    def get(self, request):
        """Return the version of the current running app"""
        data = {"version": settings.VERSION}
        return Response(data, status.HTTP_200_OK)


class LoginView(APIView):

    throttle_classes = [throttles.LoginThrottle]

    def post(self, request):
        """Login by creating a user with the given name and random password"""

        serializer = serializers.LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data["name"]

        username = str(uuid.uuid4())
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=32))

        user = User.objects.create_user(username=username, password=password, first_name=name)
        token, created = Token.objects.get_or_create(user=user)

        response_data = {
            'id': username,
            'name': name,
            'token': token.key,
        }

        return Response(status=200, data=response_data)


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

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['board', 'lane', 'owner']
    ordering_fields = ['position']
    ordering = ['position']
