
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions allowed for anyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions only for owner
        return obj.author == request.user