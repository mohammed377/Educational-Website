from rest_framework import serializers
from .models import Course, Lesson, Enrollment, Quiz, Question, Answer, DiscussionForum, Comment, Resource, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'profile_picture', 'bio', 'social_media_links']

class BaseSerializer(serializers.ModelSerializer):
    """
    Base serializer class with all fields included.
    """
    class Meta:
        abstract = True
        fields = '__all__'

class CourseSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Course

class LessonSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Lesson

class EnrollmentSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Enrollment

class QuizSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Quiz

class QuestionSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Question

class AnswerSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Answer

class DiscussionForumSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = DiscussionForum

class CommentSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Comment

class ResourceSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Resource

class EnrolledCoursesSerializer(serializers.ModelSerializer):
    """
    Serializer for listing enrolled courses.
    """
    class Meta:
        model = Enrollment
        fields = ['course']  # Adjust fields as needed
