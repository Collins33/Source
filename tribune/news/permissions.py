from rest_framework.permissions import SAFE_METHODS,BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self,request,view):
        if request.method i SAFE_METHODS:
            return True
    else:
        return request.user.is_staff
