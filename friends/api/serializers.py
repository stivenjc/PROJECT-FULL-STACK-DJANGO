from rest_framework.serializers import ModelSerializer

from friends.models import Friends
from users.api.serializers import UserSerializer


class FriendsSerializers(ModelSerializer):
    transmitter_data = UserSerializer(source='transmitter', read_only=True)
    receiver_data = UserSerializer(source='receiver', read_only=True)

    class Meta:
        model = Friends
        fields = ['id', 'friend', 'transmitter', 'transmitter_data', 'receiver', 'receiver_data']
