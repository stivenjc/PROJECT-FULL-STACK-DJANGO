
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from users.api.serializers import UserSerializer
from users.models import User

class GetMeTest(APITestCase):

    """
    verifica que deveulva los datos del usuario logeado
    """

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='testuser@example.com'
        )
        self.client.force_authenticate(user=self.user)

    def test_get_me(self):
        url = reverse('users:getme')
        print(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user_serializer = UserSerializer(self.user)
        self.assertEqual(response.data, user_serializer.data)