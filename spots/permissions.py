from rest_framework import permissions


class UserIsAuthorized(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            print()
            print(request.user.id)
            print()
            return True
