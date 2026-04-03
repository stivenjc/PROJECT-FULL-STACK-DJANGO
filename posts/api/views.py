from django.db.models import Q
from requests import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from friends.models import Friends
from posts.api.serializers import PostsSerializers
from posts.models import Posts


class PostsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        friend_only = self.request.query_params.get('friends_only', False)

        if friend_only == 'true':
            friends_qs = Friends.objects.filter(
                transmitter=self.request.user,
                friend=True
            )

            r_ids = list(friends_qs.values_list('receiver_id', flat=True))

            all_ids = set(r_ids + [self.request.user.id])

            return Posts.objects.filter(created_by__in=all_ids).order_by('-created')
        return Posts.objects.all().order_by('-created')

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['created_by']
    serializer_class = PostsSerializers
