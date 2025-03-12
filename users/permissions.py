from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """
    Custom permission to only allow users to access their own data.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the user is trying to access their own data
        return obj.user.id == request.user.id
