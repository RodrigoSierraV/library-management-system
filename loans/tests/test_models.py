from datetime import datetime

from django.test import TestCase
from django.contrib.auth import get_user_model
from books.models import Book
from loans.models import Loan

User = get_user_model()

class LoanModelTest(TestCase):
    def test_create_loan(self):
        user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='password123'
        )
        book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            isbn='1234567890',
            published_date='2020-01-01',
            available=True,
            page_count=100
        )
        loan = Loan.objects.create(
            user=user,
            book=book,
            borrowed_at='2023-01-01'
        )
        self.assertEqual(loan.user, user)
        self.assertEqual(loan.book, book)
        self.assertIsNone(loan.returned_at)
        self.assertEqual(str(loan), f"{user.username} borrowed {book.title}")
