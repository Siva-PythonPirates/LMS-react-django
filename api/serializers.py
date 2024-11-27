from rest_framework import serializers
from .models import Course, Lesson, Quiz, Enrollment

class CourseSerializer(serializers.ModelSerializer):
    lessons = serializers.StringRelatedField(many=True)

    class Meta:
        model = Course
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'
