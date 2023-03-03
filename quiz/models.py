from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

class Question(models.Model):
    text = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

class Answer(models.Model):
    text = models.TextField()
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

class UserQuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.FloatField()
