from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLES)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True)
    social_media_links = models.URLField(blank=True)
    
    def __str__(self):
        return self.user.username

class Course(models.Model):
    LEVELS = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField(help_text="Duration in hours")
    instructor = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=LEVELS)
    category = models.CharField(max_length=50)
    
class Lesson(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    video_url = models.URLField(blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

class Enrollment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    completion_status = models.BooleanField(default=False)

class Quiz(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    passing_score = models.FloatField()

class Question(models.Model):
    text = models.TextField()
    options = models.JSONField()
    correct_option = models.IntegerField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

class Answer(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.IntegerField()
    submission_time = models.DateTimeField(auto_now_add=True)

class DiscussionForum(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    content = models.TextField()
    discussion = models.ForeignKey(DiscussionForum, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

class Resource(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='resources/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
