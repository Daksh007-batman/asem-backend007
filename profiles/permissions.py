from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        if (request.method in SAFE_METHODS):
            return True
        print(request.user.role)
        return request.user.role == 'superadmin'