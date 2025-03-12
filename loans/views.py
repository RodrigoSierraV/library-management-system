from django.utils.timezone import now
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from books.models import Book
from users.permissions import IsOwner
from loans.serializers import LoanSerializer
from loans.permissions import IsBorrower
from loans.models import Loan


class BorrowBookView(generics.CreateAPIView):
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        book_id = serializer.validated_data['book_id']
        book = Book.objects.get(id=book_id)
        book.available = False
        book.save()
        serializer.save(user=self.request.user)


class ReturnBookView(generics.UpdateAPIView):
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated, IsBorrower]
    http_method_names = ['patch']

    def get_object(self):
        book_id = self.request.data.get('book_id')
        if not book_id:
            raise generics.ValidationError("book_id is required.")
        loan = Loan.objects.filter(book_id=book_id, returned_at__isnull=True).first()
        if loan is None:
            raise generics.Http404("No active loan found for this book.")
        self.check_object_permissions(self.request, loan)
        return loan

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.book.available = True
        instance.book.save()
        instance.returned_at = now()
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
