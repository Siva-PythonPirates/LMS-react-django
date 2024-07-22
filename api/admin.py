# admin.py
from django.contrib import admin
from .models import Course, Lesson, Quiz, Enrollment

# Register your models here.
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Quiz)
admin.site.register(Enrollment)