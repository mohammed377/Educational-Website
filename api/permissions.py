from rest_framework.permissions import BasePermission
from .models import Enrollment


class IsTeacherOrAdmin(BasePermission):
    """
    Custom permission to only allow teachers or admins to create courses.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.userprofile.role == 'teacher' or request.user.userprofile.role == 'admin')

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to only allow admins to perform write operations.
    """
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user.is_authenticated and request.user.userprofile.role == 'admin'

class IsTeacherOrReadOnly(BasePermission):
    """
    Custom permission to allow students or normal users to view courses but not create them.
    """
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return False  # Deny permission for creating courses


class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Instance must have an attribute named `owner`.
        return obj.user == request.user


class IsEnrolled(BasePermission):
    """
    Custom permission to only allow enrolled users to see lessons of a course.
    """
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False

        # Assuming the course_id is passed in the view kwargs
        course_id = view.kwargs.get('course_id')
        
        # Check if the user is enrolled in the course
        if Enrollment.objects.filter(user=request.user.userprofile, course_id=course_id).exists():
            return True
        else:
            return False
