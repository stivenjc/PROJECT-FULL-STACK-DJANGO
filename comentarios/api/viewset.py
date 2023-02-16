from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from comentarios.api.serializers import ComentSerializers
from comentarios.models import Comment


class ComentVieeSet(ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = ComentSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']
