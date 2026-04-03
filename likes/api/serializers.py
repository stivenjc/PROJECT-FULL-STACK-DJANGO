from rest_framework.serializers import ModelSerializer

from likes.models import Likes


class LikesSerializers(ModelSerializer):
    class Meta:
        model = Likes
        fields = ['id', 'post', 'user']
        extra_kwargs = {'user': {'read_only': True}}

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        return super().create(validated_data)
