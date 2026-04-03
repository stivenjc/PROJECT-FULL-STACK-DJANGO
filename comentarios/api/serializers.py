from rest_framework.serializers import ModelSerializer

from comentarios.models import Comment
from users.api.serializers import UserSerializer


class ComentSerializers(ModelSerializer):
    created_data = UserSerializer(source='created', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'created_data', 'created', 'title', 'post', 'modified', ]
        extra_kwargs = {
            'created': {'required': False},
            'title': {'required': True},
            'post': {'required': False}
        }

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['created'] = request.user
        return super().create(validated_data)
