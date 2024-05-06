from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.utils.translation import gettext_lazy as _
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsTeacherOrReadOnly,IsAdminOrReadOnly,IsOwnerOrReadOnly,IsEnrolled
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
#from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .permissions import IsTeacherOrAdmin, IsTeacherOrReadOnly

User = get_user_model()

#User authentication views
class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=request.data['username'])
            user.set_password(request.data['password'])
            user.save()
            token = Token.objects.get_or_create(user=user)
            return Response({"token": token.key,"user":serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user = get_object_or_404(User,username=request.data['username'])
        if not user.check_password(request.data['password']):
            return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]  # Apply IsOwnerOrReadOnly permission

    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)

class UpdateUserAPIView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]  # Apply IsOwnerOrReadOnly permission

    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# CRUD operations views for different models 
class ModelListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated,IsTeacherOrAdmin]  # Apply IsOwnerOrReadOnly permission

    queryset = None
    serializer_class = None

    def get_queryset(self):
        return self.queryset.all()

    def get_serializer_class(self):
        return self.serializer_class


class ModelRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]  # Apply IsOwnerOrReadOnly permission

    queryset = None
    serializer_class = None

    def get_queryset(self):
        return self.queryset.all()

    def get_serializer_class(self):
        return self.serializer_class



class CourseListCreate(ModelListCreate):
    permission_classes = [IsAuthenticated,IsTeacherOrReadOnly] 

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseRetrieveUpdateDestroy(ModelRetrieveUpdateDestroy):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonListCreate(ModelListCreate):
    permission_classes = [IsEnrolled,IsTeacherOrReadOnly]  # Only authenticated users can view enrolled courses

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonRetrieveUpdateDestroy(ModelRetrieveUpdateDestroy):

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class EnrollmentListCreate(ModelListCreate):
    permission_classes = [IsAuthenticated]  # Only authenticated users can view enrolled courses

    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class EnrollmentRetrieveUpdateDestroy(ModelRetrieveUpdateDestroy):

    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class QuizListCreate(ModelListCreate):
    permission_classes = [IsAuthenticated,(IsTeacherOrAdmin|IsEnrolled)]  


    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuizRetrieveUpdateDestroy(ModelRetrieveUpdateDestroy):

    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuestionListCreate(ModelListCreate):
    permission_classes = [IsAuthenticated,(IsTeacherOrAdmin|IsEnrolled)]  

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionRetrieveUpdateDestroy(ModelRetrieveUpdateDestroy):

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerListCreate(ModelListCreate):

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerRetrieveUpdateDestroy(ModelRetrieveUpdateDestroy):
    permission_classes = [IsAuthenticated, IsTeacherOrReadOnly,IsOwnerOrReadOnly]  # Apply IsOwnerOrReadOnly permission

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class DiscussionForumListCreate(ModelListCreate):
    permission_classes = ModelListCreate.permission_classes or [IsAuthenticated,IsTeacherOrReadOnly]  # Only authenticated users can view enrolled courses

    queryset = DiscussionForum.objects.all()
    serializer_class = DiscussionForumSerializer


class DiscussionForumRetrieveUpdateDestroy(ModelRetrieveUpdateDestroy):

    queryset = DiscussionForum.objects.all()
    serializer_class = DiscussionForumSerializer


class CommentListCreate(ModelListCreate):
    permission_classes = [IsAuthenticatedOrReadOnly,IsEnrolled]  # Only authenticated users can view enrolled courses

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetrieveUpdateDestroy(ModelRetrieveUpdateDestroy):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ResourceListCreate(ModelListCreate):
    permission_classes = [IsAuthenticated,(IsTeacherOrAdmin|IsEnrolled)]  

    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


class ResourceRetrieveUpdateDestroy(ModelRetrieveUpdateDestroy):

    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


class EnrolledCoursesView(generics.ListAPIView):
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]  # Apply IsOwnerOrReadOnly permission

    serializer_class = EnrolledCoursesSerializer


    def get_queryset(self):
        return Enrollment.objects.filter(user=self.request.user)
