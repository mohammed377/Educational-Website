from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import (
    Course, Lesson, Enrollment, Quiz, Question, Answer, 
    DiscussionForum, Comment, Resource
)
from .serializers import (
    UserSerializer, CourseSerializer, LessonSerializer, EnrollmentSerializer, 
    QuizSerializer, QuestionSerializer, AnswerSerializer, 
    DiscussionForumSerializer, CommentSerializer, ResourceSerializer, EnrolledCoursesSerializer
)
from rest_framework.response import Response

User = get_user_model()

class ChangePasswordView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PasswordChangeForm

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = request.user
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            # Update session authentication hash to prevent logout
            update_session_auth_hash(request, user)
            return Response({'status': 'password changed'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileUpdateView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class ModelListCreate(generics.ListCreateAPIView):
    queryset = None
    serializer_class = None

    def get_queryset(self):
        return self.queryset.all()

    def get_serializer_class(self):
        return self.serializer_class


class ModelRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = None
    serializer_class = None

    def get_queryset(self):
        return self.queryset.all()

    def get_serializer_class(self):
        return self.serializer_class


class CourseListCreate(ModelListCreate):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseRetrieveUpdateDestroy(ModelRetrieveUpdateDestroy):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonListCreate(ModelListCreate):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonRetrieveUpdateDestroy(ModelRetrieveUpdateDestroy):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class EnrollmentListCreate(ModelListCreate):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class EnrollmentRetrieveUpdateDestroy(ModelRetrieveUpdateDestroy):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class QuizListCreate(ModelListCreate):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuizRetrieveUpdateDestroy(ModelRetrieveUpdateDestroy):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuestionListCreate(ModelListCreate):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionRetrieveUpdateDestroy(ModelRetrieveUpdateDestroy):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerListCreate(ModelListCreate):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerRetrieveUpdateDestroy(ModelRetrieveUpdateDestroy):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class DiscussionForumListCreate(ModelListCreate):
    queryset = DiscussionForum.objects.all()
    serializer_class = DiscussionForumSerializer


class DiscussionForumRetrieveUpdateDestroy(ModelRetrieveUpdateDestroy):
    queryset = DiscussionForum.objects.all()
    serializer_class = DiscussionForumSerializer


class CommentListCreate(ModelListCreate):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetrieveUpdateDestroy(ModelRetrieveUpdateDestroy):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ResourceListCreate(ModelListCreate):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


class ResourceRetrieveUpdateDestroy(ModelRetrieveUpdateDestroy):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


class EnrolledCoursesView(generics.ListAPIView):
    serializer_class = EnrolledCoursesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Enrollment.objects.filter(user=self.request.user)
