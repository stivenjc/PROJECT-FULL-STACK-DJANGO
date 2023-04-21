from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from friends.models import Friends
from friends.api.serializers import FriendsSerializers
from users.models import User


class FriendViewSetTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='testuser1', password='testpass', email='jidne@gmail.com')
        self.user2 = User.objects.create_user(
            username='testuser2', password='testpass', email='jidxdne@gmail.com')
        self.user3 = User.objects.create_user(
            username='testuser3', password='testpass', email='jidndde@gmail.com')
        self.client.force_authenticate(user=self.user1)

    def test_list_friends(self):
        """
        Verifica que se puedan listar todos los amigos.
        """
        Friends.objects.create(friend=False, transmitter=self.user1, receiver=self.user2)
        Friends.objects.create(friend=False, transmitter=self.user3, receiver=self.user1)
        url = reverse('friends:friend')
        response = self.client.get(url, format='json')
        friends = Friends.objects.all()
        serializer = FriendsSerializers(friends, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)