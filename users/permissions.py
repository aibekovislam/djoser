from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerProfileReadOnly(BasePermission):
    def have_object_permissions(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user==request.user