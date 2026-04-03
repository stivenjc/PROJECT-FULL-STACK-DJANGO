from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from comentarios.api.serializers import ComentSerializers
from posts.models import Posts
from users.api.serializers import UserSerializer


class PostsSerializers(ModelSerializer):
    created_data = UserSerializer(source='created_by', read_only=True)
    comments = ComentSerializers(many=True, read_only=True)
    likes_count = SerializerMethodField()
    has_liked = SerializerMethodField()

    class Meta:
        model = Posts
        fields = ['id', 'created_by', 'created_data', 'image', 'text', 'created', 'modified', 'comments', 'likes_count',
                  'has_liked']
        extra_kwargs = {
            'created_by': {'required': False},
            'text': {'required': False},
        }

    def get_likes_count(self, obj):
        return obj.likes_set.count()

    def get_has_liked(self, obj):
        user = self.context['request'].user
        return obj.likes_set.filter(user=user).exists()

    def create(self, validated_data):
        user = self.context['request'].user
        return Posts.objects.create(created_by=user, **validated_data)
