from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course, Lesson, Quiz, Enrollment
from .serializers import CourseSerializer, LessonSerializer, QuizSerializer, EnrollmentSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        name = request.data.get("name")  # Frontend sends `name`
        email = request.data.get("email")
        password = request.data.get("password")
        confirm_password = request.data.get("confirmPassword")

        # Validate fields
        if not all([name, email, password, confirm_password]):
            return Response({"error": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)

        if password != confirm_password:
            return Response({"error": "Passwords do not match."}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            return Response({"error": "Email is already registered."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Map `name` to `username` since `User` requires `username`
            user = User.objects.create_user(username=request.data.get("name"), email=email, password=password)
            print(f"Name: {name}, Email: {email}")

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Optionally create a token for the user
        token, _ = Token.objects.get_or_create(user=user)

        return Response(
            {
                "message": "User registered successfully.",
                "token": token.key,
                "user": {"id": user.id, "username": user.username, "email": user.email},
            },
            status=status.HTTP_201_CREATED,
        )


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        user = authenticate(username=email, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email
                }
            })
        return Response(
            {'error': 'Invalid credentials'}, 
            status=status.HTTP_401_UNAUTHORIZED
        )

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if User.objects.filter(email=email).exists():
            return Response(
                {'error': 'Email already exists'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email
            }
        }, status=status.HTTP_201_CREATED)

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

class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailAPIView(generics.RetrieveAPIView):
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

class LessonDetailAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    lookup_field = 'LessonId'

class QuizDetailAPIView(generics.RetrieveAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    lookup_field = 'QuizId'

class EnrollmentDetailAPIView(generics.RetrieveAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    lookup_field = 'EnrollmentId'
