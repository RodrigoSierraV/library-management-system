from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()

class UserViewSetTest(APITestCase):
    def test_user_registration(self):
        url = reverse('user-register')
        user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password123',
            'first_name': 'Test',
            'last_name': 'User'
        }
        response = self.client.post(url, user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')
