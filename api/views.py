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
from django.views.decorators.csrf import csrf_exempt
# views.py
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model, authenticate, login, logout
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsTeacherOrReadOnly, IsAdminOrReadOnly, IsOwnerOrReadOnly, IsEnrolled
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404

User = get_user_model()


class RegisterAPIView(APIView):
    """
    User Registration API View
    ---
    This endpoint allows users to register by providing their username and password.
    - `username`: The username for the new user.
    - `password`: The password for the new user.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=request.data['username'])
            user.set_password(request.data['password'])
            user.save()
            token = Token.objects.get_or_create(user=user)
            return Response({"Authorization": token.key, "user": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    """
    User Login API View
    ---
    This endpoint allows users to login by providing their username and password.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        user = get_object_or_404(User, username=request.data['username'])
        if not user.check_password(request.data['password']):
            return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"Authorization": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutAPIView(APIView):
    """
    User Logout API View
    ---
    This endpoint allows authenticated users to logout.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)

class UpdateUserAPIView(APIView):
    """
    Update User API View
    ---
    This endpoint allows authenticated users to update their profile information.
    """
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ModelListCreate(generics.ListCreateAPIView):
    """
    List and Create Model API View
    ---
    This endpoint allows listing and creating instances of the specified model.
    """
    permission_classes = [IsAuthenticated, IsTeacherOrAdmin]

    queryset = None
    serializer_class = None

    def get_queryset(self):
        return self.queryset.all()

    def get_serializer_class(self):
        return self.serializer_class

class ModelRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update, and Destroy Model API View
    ---
    This endpoint allows retrieving, updating, and deleting instances of the specified model.
    """
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    queryset = None
    serializer_class = None

    def get_queryset(self):
        return self.queryset.all()

    def get_serializer_class(self):
        return self.serializer_class

class CourseListCreate(ModelListCreate):
    """
    List and Create Course API View
    ---
    This endpoint allows listing and creating courses.
    """
    permission_classes = [IsAuthenticated, IsTeacherOrReadOnly]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseRetrieveUpdateDestroy(ModelRetrieveUpdateDestroy):
    """
    Retrieve, Update, and Destroy Course API View
    ---
    This endpoint allows retrieving, updating, and deleting courses.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class LessonListCreate(ModelListCreate):
    """
    List and Create Lesson API View
    ---
    This endpoint allows listing and creating lessons.
    """
    permission_classes = [IsEnrolled, IsTeacherOrReadOnly]

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonRetrieveUpdateDestroy(ModelRetrieveUpdateDestroy):
    """
    Retrieve, Update, and Destroy Lesson API View
    ---
    This endpoint allows retrieving, updating, and deleting lessons.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class EnrollmentListCreate(ModelListCreate):
    """
    List and Create Enrollment API View
    ---
    This endpoint allows listing and creating enrollments.
    """
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class EnrollmentRetrieveUpdateDestroy(ModelRetrieveUpdateDestroy):
    """
    Retrieve, Update, and Destroy Enrollment API View
    ---
    This endpoint allows retrieving, updating, and deleting enrollments.
    """
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class QuizListCreate(ModelListCreate):
    """
    List and Create Quiz API View
    ---
    This endpoint allows listing and creating quizzes.
    """
    permission_classes = [IsAuthenticated, (IsTeacherOrAdmin | IsEnrolled)]

    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuizRetrieveUpdateDestroy(ModelRetrieveUpdateDestroy):
    """
    Retrieve, Update, and Destroy Quiz API View
    ---
    This endpoint allows retrieving, updating, and deleting quizzes.
    """
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuestionListCreate(ModelListCreate):
    """
    List and Create Question API View
    ---
    This endpoint allows listing and creating questions.
    """
    permission_classes = [IsAuthenticated, (IsTeacherOrAdmin | IsEnrolled)]

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionRetrieveUpdateDestroy(ModelRetrieveUpdateDestroy):
    """
    Retrieve, Update, and Destroy Question API View
    ---
    This endpoint allows retrieving, updating, and deleting questions.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerListCreate(ModelListCreate):
    """
    List and Create Answer API View
    ---
    This endpoint allows listing and creating answers.
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class AnswerRetrieveUpdateDestroy(ModelRetrieveUpdateDestroy):
    """
    Retrieve, Update, and Destroy Answer API View
    ---
    This endpoint allows retrieving, updating, and deleting answers.
    """
    permission_classes = [IsAuthenticated, IsTeacherOrReadOnly, IsOwnerOrReadOnly]

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class DiscussionForumListCreate(ModelListCreate):
    """
    List and Create Discussion Forum API View
    ---
    This endpoint allows listing and creating discussion forums.
    """
    permission_classes = [IsAuthenticated, IsTeacherOrReadOnly]

    queryset = DiscussionForum.objects.all()
    serializer_class = DiscussionForumSerializer

class DiscussionForumRetrieveUpdateDestroy(ModelRetrieveUpdateDestroy):
    """
    Retrieve, Update, and Destroy Discussion Forum API View
    ---
    This endpoint allows retrieving, updating, and deleting discussion forums.
    """
    queryset = DiscussionForum.objects.all()
    serializer_class = DiscussionForumSerializer

class CommentListCreate(ModelListCreate):
    """
    List and Create Comment API View
    ---
    This endpoint allows listing and creating comments.
    """
    permission_classes = [IsAuthenticatedOrReadOnly, IsEnrolled]

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentRetrieveUpdateDestroy(ModelRetrieveUpdateDestroy):
    """
    Retrieve, Update, and Destroy Comment API View
    ---
    This endpoint allows retrieving, updating, and deleting comments.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ResourceListCreate(ModelListCreate):
    """
    List and Create Resource API View
    ---
    This endpoint allows listing and creating resources.
    """
    permission_classes = [IsAuthenticated, (IsTeacherOrAdmin | IsEnrolled)]

    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

class ResourceRetrieveUpdateDestroy(ModelRetrieveUpdateDestroy):
    """
    Retrieve, Update, and Destroy Resource API View
    ---
    This endpoint allows retrieving, updating, and deleting resources.
    """
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

class EnrolledCoursesView(generics.ListAPIView):
    """
    List Enrolled Courses API View
    ---
    This endpoint allows authenticated users to view their enrolled courses.
    """
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    serializer_class = EnrolledCoursesSerializer

    def get_queryset(self):
        return Enrollment.objects.filter(user=self.request.user.userprofile)
