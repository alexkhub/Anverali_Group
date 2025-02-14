from rest_framework import permissions


class ProfilePermissions(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or request.methode in permissions.SAFE_METHODS:
            return True
        return False
