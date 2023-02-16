from rest_framework.serializers import ModelSerializer

from comentarios.models import Comment
from users.api.serializers import UserSerializer


class ComentSerializers(ModelSerializer):
    created_data = UserSerializer(source='created', read_only=True)
    class Meta:
        model = Comment
        fields = ['id','created_data', 'created', 'title', 'post', 'modified',]
