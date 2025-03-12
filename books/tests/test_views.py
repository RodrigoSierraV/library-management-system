from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from books.models import Book

class BookListViewTest(APITestCase):
    def setUp(self):
        Book.objects.create(
            title='Test Book 1',
            author='Test Author',
            isbn='1234567890',
            published_date='2020-01-01',
            available=True,
            page_count=100
        )
        Book.objects.create(
            title='Test Book 2',
            author='Test Author',
            isbn='1234567891',
            published_date='2020-01-02',
            available=True,
            page_count=150
        )

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['results'][0]['title'], 'Test Book 1')
        self.assertEqual(response.data['results'][1]['title'], 'Test Book 2')

    def test_filter_books_by_title(self):
        url = reverse('book-list') + '?title=Test%20Book%201'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'Test Book 1')
