from rest_framework.permissions import BasePermission, IsAuthenticated

class IsTeacherOrReadOnly(BasePermission):
    """
    Custom permission to only allow teachers to create courses.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'teacher'

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to only allow admins to perform write operations.
    """
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user.is_authenticated and request.user.role == 'admin'
