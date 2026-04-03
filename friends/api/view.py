from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from friends.api.serializers import FriendsSerializers
from friends.models import Friends


class FriendViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Friends.objects.all()
    serializer_class = FriendsSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['friend', 'transmitter', 'receiver']

    @action(detail=False, methods=['get'], url_path='my-friends')
    def my_friends(self, request):
        user = request.user
        friends = Friends.objects.filter(
            transmitter=user,
            friend=True
        )

        serializer = FriendsSerializers(friends, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='check-friend/(?P<user_id>\d+)')
    def check_friend_status(self, request, user_id):
        current_user = request.user

        friendship = Friends.objects.filter(
            (Q(transmitter=current_user) & Q(receiver_id=user_id))
        ).first()
        if not friendship:
            return Response({'status': 'none'})
        if friendship.friend:
            return Response({
                'status': 'fallowing',
                'id': friendship.id
            })
        else:
            if friendship.transmitter == current_user:
                return Response({
                    'status': 'pending_sent',
                    'id': friendship.id
                })
            else:
                return Response({
                    'status': 'pending_received',
                    'id': friendship.id
                })

    @action(detail=False, methods=['get'], url_path='fallow/(?P<user_id>\d+)')
    def fallowing_and_fallowers(self, request, user_id):
        fallowers = Friends.objects.filter(receiver=user_id, friend=True).count()
        fallowing = Friends.objects.filter(transmitter=user_id, friend=True).count()
        return Response({'fallowers': fallowers, 'fallowing': fallowing}, status=status.HTTP_200_OK)
