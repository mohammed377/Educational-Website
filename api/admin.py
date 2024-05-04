from django.contrib import admin
from .models import (
    Course, Lesson, Enrollment, Quiz, Question, Answer, 
    DiscussionForum, Comment, Resource, User
)

# Register your models here
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Enrollment)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(DiscussionForum)
admin.site.register(Comment)
admin.site.register(Resource)
admin.site.register(User)  # Assuming this is your custom User model
