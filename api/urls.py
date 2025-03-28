from .views import complete_lesson
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('auth/login/', views.LoginView.as_view(), name='login'),
    path('auth/register/', views.RegisterView.as_view(), name='register'),
    path('courses/', views.CourseListAPIView.as_view()),
    path('courses/create/', views.CourseCreateAPIView.as_view()),
    path('courses/<int:CourseId>/', views.CourseDetailAPIView.as_view()),
    path('courses/<int:CourseId>/update/', views.CourseUpdateAPIView.as_view()),
    path('courses/<int:CourseId>/delete/', views.CourseDeleteAPIView.as_view()),
    path('lessons/', views.LessonListAPIView.as_view()),
    path('lessons/create/', views.LessonCreateAPIView.as_view()),
    path('lessons/<int:LessonId>/', views.LessonDetailAPIView.as_view()),
    path('lessons/<int:LessonId>/update/', views.LessonUpdateAPIView.as_view()),
    path('lessons/<int:LessonId>/delete/', views.LessonDeleteAPIView.as_view()),
    path('quizzes/', views.QuizListAPIView.as_view()),
    path('quizzes/create/', views.QuizCreateAPIView.as_view()),
    path('quizzes/<int:QuizId>/', views.QuizDetailAPIView.as_view()),
    path('quizzes/<int:QuizId>/update/', views.QuizUpdateAPIView.as_view()),
    path('quizzes/<int:QuizId>/delete/', views.QuizDeleteAPIView.as_view()),
    path('enrollments/', views.EnrollmentListAPIView.as_view()),
    path('enrollments/create/', views.EnrollmentCreateAPIView.as_view()),
    path('enrollments/<int:EnrollmentId>/', views.EnrollmentDetailAPIView.as_view()),
    path('enrollments/<int:EnrollmentId>/update/', views.EnrollmentUpdateAPIView.as_view()),
    path('enrollments/<int:EnrollmentId>/delete/', views.EnrollmentDeleteAPIView.as_view()),
    path("lessons/<int:lesson_id>/complete/", complete_lesson, name="complete-lesson"),
]