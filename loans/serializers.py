from rest_framework import serializers
from .models import Loan
from books.models import Book


class LoanSerializer(serializers.ModelSerializer):
    book_id = serializers.IntegerField()

    class Meta:
        model = Loan
        fields = ['id', 'book_id', 'borrowed_at', 'returned_at', 'user_id']
        read_only_fields = ['id', 'borrowed_at', 'returned_at', 'user_id', 'book_id']

    def validate_book_id(self, value):
        try:
            book = Book.objects.get(id=value)
        except Book.DoesNotExist:
            raise serializers.ValidationError("Book does not exist.")
        if not book.available:
            raise serializers.ValidationError("This book is not available for borrowing.")
        return value
