from rest_framework.serializers import ModelSerializer

from likes.models import Likes


class LikesSerializers(ModelSerializer):
    class Meta:
        model = Likes
        fields = ['id', 'post', 'user']
