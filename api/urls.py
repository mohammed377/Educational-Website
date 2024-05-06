from django.urls import path
from .views import (
    CourseListCreate, CourseRetrieveUpdateDestroy,
    LessonListCreate, LessonRetrieveUpdateDestroy,
    EnrollmentListCreate, EnrollmentRetrieveUpdateDestroy,
    QuizListCreate, QuizRetrieveUpdateDestroy,
    QuestionListCreate, QuestionRetrieveUpdateDestroy,
    AnswerListCreate, AnswerRetrieveUpdateDestroy,
    DiscussionForumListCreate, DiscussionForumRetrieveUpdateDestroy,
    CommentListCreate, CommentRetrieveUpdateDestroy,
    ResourceListCreate, ResourceRetrieveUpdateDestroy,
    EnrolledCoursesView,RegisterAPIView, LoginAPIView, LogoutAPIView, UpdateUserAPIView
)

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('update/', UpdateUserAPIView.as_view(), name='update'),


    path('courses/', CourseListCreate.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseRetrieveUpdateDestroy.as_view(), name='course-detail'),

    path('lessons/', LessonListCreate.as_view(), name='lesson-list-create'),
    path('lessons/<int:pk>/', LessonRetrieveUpdateDestroy.as_view(), name='lesson-detail'),

    path('enrollments/', EnrollmentListCreate.as_view(), name='enrollment-list-create'),
    path('enrollments/<int:pk>/', EnrollmentRetrieveUpdateDestroy.as_view(), name='enrollment-detail'),

    path('quizzes/', QuizListCreate.as_view(), name='quiz-list-create'),
    path('quizzes/<int:pk>/', QuizRetrieveUpdateDestroy.as_view(), name='quiz-detail'),

    path('questions/', QuestionListCreate.as_view(), name='question-list-create'),
    path('questions/<int:pk>/', QuestionRetrieveUpdateDestroy.as_view(), name='question-detail'),

    path('answers/', AnswerListCreate.as_view(), name='answer-list-create'),
    path('answers/<int:pk>/', AnswerRetrieveUpdateDestroy.as_view(), name='answer-detail'),

    path('discussion-forums/', DiscussionForumListCreate.as_view(), name='discussionforum-list-create'),
    path('discussion-forums/<int:pk>/', DiscussionForumRetrieveUpdateDestroy.as_view(), name='discussionforum-detail'),

    path('comments/', CommentListCreate.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroy.as_view(), name='comment-detail'),

    path('resources/', ResourceListCreate.as_view(), name='resource-list-create'),
    path('resources/<int:pk>/', ResourceRetrieveUpdateDestroy.as_view(), name='resource-detail'),

    path('enrolled-courses/', EnrolledCoursesView.as_view(), name='enrolled-courses-list'),
]
