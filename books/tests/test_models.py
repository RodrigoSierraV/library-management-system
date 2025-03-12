from django.test import TestCase
from books.models import Book

class BookModelTest(TestCase):
    def test_create_book(self):
        book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            isbn='1234567890',
            published_date='2020-01-01',
            available=True,
            page_count=100
        )
        self.assertEqual(book.title, 'Test Book')
        self.assertEqual(book.author, 'Test Author')
        self.assertEqual(book.isbn, '1234567890')
        self.assertTrue(book.available)
        self.assertEqual(str(book), "Test Book")
