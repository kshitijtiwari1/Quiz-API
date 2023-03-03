from django.urls import path
from .views import QuizList, QuizDetail, UserQuizResultList

urlpatterns = [
    path('quizzes/', QuizList.as_view(), name='quiz-list'),
    path('quizzes/<int:pk>/', QuizDetail.as_view(), name='quiz-detail'),
    path('user-quiz-results/', UserQuizResultList.as_view(), name='user-quiz-result-list'),
]
