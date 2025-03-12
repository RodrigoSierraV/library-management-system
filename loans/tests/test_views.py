from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from books.models import Book
from loans.models import Loan
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class LoanViewSetTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='password123'
        )
        self.other_user = User.objects.create_user(
            username='otheruser',
            email='otheruser@example.com',
            password='password123'
        )
        self.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            isbn='1234567890',
            published_date='2020-01-01',
            page_count=100,
            available=True
        )
        self.client.login(username='testuser', password='password123')
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)

    def test_borrow_book(self):
        url = reverse('borrow-book')
        loan_data = {
            'book_id': self.book.id
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.post(url, loan_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.book.refresh_from_db()
        self.assertFalse(self.book.available)
        self.assertEqual(Loan.objects.count(), 1)
        self.assertEqual(Loan.objects.get().user, self.user)

    def test_return_book(self):
        loan = Loan.objects.create(
            user=self.user,
            book=self.book,
            borrowed_at='2023-01-01'
        )
        url = reverse('return-book')
        return_data = {
            'book_id': self.book.id
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.patch(url, return_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertTrue(self.book.available)
        loan.refresh_from_db()
        self.assertIsNotNone(loan.returned_at)
    
    def test_borrow_unavailable_book(self):
        # Mark the book as unavailable
        self.book.available = False
        self.book.save()

        url = reverse('borrow-book')
        loan_data = {
            'book_id': self.book.id
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.post(url, loan_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['book_id'][0], "This book is not available for borrowing.")
        self.assertEqual(Loan.objects.count(), 0)

    def test_return_book_borrowed_by_other_user(self):
        loan = Loan.objects.create(
            user=self.other_user,
            book=self.book,
            borrowed_at='2023-01-01'
        )
        url = reverse('return-book')
        return_data = {
            'book_id': self.book.id
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.patch(url, return_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['detail'], "You do not have permission to perform this action.")
