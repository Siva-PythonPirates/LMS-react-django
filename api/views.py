# views.py
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course, Lesson, Quiz, Enrollment
from .serializers import CourseSerializer, LessonSerializer, QuizSerializer, EnrollmentSerializer

class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseCreateAPIView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDeleteAPIView(generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'CourseId'

class CourseUpdateAPIView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'CourseId'

class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonCreateAPIView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LessonDeleteAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    lookup_field = 'LessonId'

class LessonUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    lookup_field = 'LessonId'

class QuizListAPIView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuizCreateAPIView(generics.CreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuizDeleteAPIView(generics.DestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    lookup_field = 'QuizId'

class QuizUpdateAPIView(generics.UpdateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    lookup_field = 'QuizId'

class EnrollmentListAPIView(generics.ListAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class EnrollmentCreateAPIView(generics.CreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EnrollmentDeleteAPIView(generics.DestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    lookup_field = 'EnrollmentId'

class EnrollmentUpdateAPIView(generics.UpdateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    lookup_field = 'EnrollmentId'