# models.py
from django.db import models

# Create your models here.
class Course(models.Model):
    CourseId = models.AutoField(primary_key=True)
    CourseName = models.CharField(max_length=100)
    Description = models.TextField()
    StartDate = models.DateField()
    EndDate = models.DateField()
    def __str__(self) -> str:
        return self.CourseName

class Lesson(models.Model):
    LessonId = models.AutoField(primary_key=True)
    LessonName = models.CharField(max_length=100)
    Description = models.TextField()
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.LessonName

class Quiz(models.Model):
    QuizId = models.AutoField(primary_key=True)
    QuizName = models.CharField(max_length=100)
    Description = models.TextField()
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.QuizName

class Enrollment(models.Model):
    EnrollmentId = models.AutoField(primary_key=True)
    Student = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    StartDate = models.DateField()
    EndDate = models.DateField()
    def __str__(self) -> str:
        return f"{self.Student.username} - {self.Course.CourseName}"

class QuizQuestion(models.Model):
    QuestionId = models.AutoField(primary_key=True)
    Quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    QuestionText = models.TextField()
    def __str__(self) -> str:
        return self.QuestionText

class QuizAnswer(models.Model):
    AnswerId = models.AutoField(primary_key=True)
    Question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    AnswerText = models.TextField()
    IsCorrect = models.BooleanField()
    def __str__(self) -> str:
        return self.AnswerText