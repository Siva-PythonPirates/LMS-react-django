# urls.py
from django.urls import path
from . import views
from .views import (
    CourseListAPIView,
    CourseCreateAPIView,
    CourseDeleteAPIView,
    CourseUpdateAPIView,
    LessonListAPIView,
    LessonCreateAPIView,
    LessonDeleteAPIView,
    LessonUpdateAPIView,
    QuizListAPIView,
    QuizCreateAPIView,
    QuizDeleteAPIView,
    QuizUpdateAPIView,
    EnrollmentListAPIView,
    EnrollmentCreateAPIView,
    EnrollmentDeleteAPIView,
    EnrollmentUpdateAPIView
)

urlpatterns = [
    path('courses/', CourseListAPIView.as_view()),
    path('courses/create/', CourseCreateAPIView.as_view()),
    path('courses/<int:CourseId>/', CourseUpdateAPIView.as_view()),
    path('courses/<int:CourseId>/delete/', CourseDeleteAPIView.as_view()),
    path('lessons/', LessonListAPIView.as_view()),
    path('lessons/create/', LessonCreateAPIView.as_view()),
    path('lessons/<int:LessonId>/', LessonUpdateAPIView.as_view()),
    path('lessons/<int:LessonId>/delete/', LessonDeleteAPIView.as_view()),
    path('quizzes/', QuizListAPIView.as_view()),
    path('quizzes/create/', QuizCreateAPIView.as_view()),
    path('quizzes/<int:QuizId>/', QuizUpdateAPIView.as_view()),
    path('quizzes/<int:QuizId>/delete/', QuizDeleteAPIView.as_view()),
    path('enrollments/', EnrollmentListAPIView.as_view()),
    path('enrollments/create/', EnrollmentCreateAPIView.as_view()),
    path('enrollments/<int:EnrollmentId>/', EnrollmentUpdateAPIView.as_view()),
    path('enrollments/<int:EnrollmentId>/delete/', EnrollmentDeleteAPIView.as_view()),
]