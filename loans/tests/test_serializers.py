from django.test import TestCase
from loans.serializers import LoanSerializer
from django.contrib.auth import get_user_model
from books.models import Book
from loans.models import Loan
from unittest import skip

User = get_user_model()


@skip("Skip until we have a better understanding of how to test this serializer")
class LoanSerializerTest(TestCase):
    def test_loan_serializer(self):
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
            page_count=100,
            available=True
        )
        loan_data = {
            'book_id': book.id,
            'borrowed_at': '2023-01-01',
            'user': user,
        }
        serializer = LoanSerializer(data=loan_data)
        serializer.is_valid()
        self.assertTrue(serializer.is_valid())
        loan = serializer.save()
        self.assertEqual(loan.user, user)
        self.assertEqual(loan.book, book)
        self.assertEqual(loan.borrowed_at, '2023-01-01')
