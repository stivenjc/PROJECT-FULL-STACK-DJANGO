from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from likes.api.serializers import LikesSerializers
from likes.models import Likes


class LikesViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Likes.objects.all()
    serializer_class = LikesSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post', 'user']
