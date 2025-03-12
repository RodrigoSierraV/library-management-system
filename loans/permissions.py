from rest_framework.permissions import BasePermission

class IsBorrower(BasePermission):
    """
    Custom permission to only allow the borrower to return the book.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
