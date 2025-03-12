from django.test import TestCase
from books.serializers import BookSerializer
from books.models import Book

class BookSerializerTest(TestCase):
    def test_book_serializer(self):
        book_data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'isbn': '1234567890',
            'published_date': '2020-01-01',
            'available': True,
            'page_count': 100
        }
        serializer = BookSerializer(data=book_data)
        serializer.is_valid()
        self.assertTrue(serializer.is_valid())
        book = serializer.save()
        self.assertEqual(book.title, 'Test Book')
        self.assertEqual(book.author, 'Test Author')
        self.assertEqual(book.isbn, '1234567890')
        self.assertTrue(book.available)
