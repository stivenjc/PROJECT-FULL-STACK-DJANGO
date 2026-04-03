from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from likes.api.serializers import LikesSerializers
from likes.models import Likes
from rest_framework import status


class LikesViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Likes.objects.all()
    serializer_class = LikesSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post', 'user']

    @action(detail=False, methods=['delete'], url_path='delete-by-post/(?P<post_id>[0-9]+)')
    def delete_by_post(self, request, post_id=None):
        # El user_id lo sacamos automáticamente del request.user (¡más seguro!)
        like = Likes.objects.filter(post_id=post_id, user=request.user).first()

        if like:
            like.delete()
            return Response({'status': 'deleted'}, status=status.HTTP_204_NO_CONTENT)

        return Response({'error': 'Like not found'}, status=status.HTTP_404_NOT_FOUND)
