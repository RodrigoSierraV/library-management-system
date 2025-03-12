from django.test import TestCase
from users.serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializerTest(TestCase):
    def test_user_serializer(self):
        user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password123',
            'first_name': 'Test',
            'last_name': 'User'
        }
        serializer = UserSerializer(data=user_data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertTrue(user.check_password('password123'))
