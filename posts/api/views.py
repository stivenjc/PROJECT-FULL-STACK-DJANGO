from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from posts.api.serializers import PostsSerializers
from posts.models import Posts


class PostsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Posts.objects.all().order_by('-created')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['created_by']
    serializer_class = PostsSerializers
