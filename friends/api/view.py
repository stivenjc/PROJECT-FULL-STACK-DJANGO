from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from friends.api.serializers import FriendsSerializers
from friends.models import Friends


class FriendViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Friends.objects.all()
    serializer_class = FriendsSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['friend', 'transmitter', 'receiver']
