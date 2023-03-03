from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Quiz, UserQuizResult
from .serializers import QuizSerializer, UserQuizResultSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

class QuizList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, TokenAuthentication, SessionAuthentication]
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuizDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, TokenAuthentication, SessionAuthentication]
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class UserQuizResultList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, TokenAuthentication, SessionAuthentication]
    serializer_class = UserQuizResultSerializer

    def get_queryset(self):
        user = self.request.user
        return UserQuizResult.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
