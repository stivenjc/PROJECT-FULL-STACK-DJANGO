from rest_framework.serializers import ModelSerializer

from posts.models import Posts
from users.api.serializers import UserSerializer


class PostsSerializers(ModelSerializer):
    created_data = UserSerializer(source='created_by', read_only=True)

    class Meta:
        model = Posts
        fields = ['id', 'created_by', 'created_data', 'image', 'text', 'created', 'modified']
