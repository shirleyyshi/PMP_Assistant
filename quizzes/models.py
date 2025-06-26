from django.db import models
from django.contrib.auth import get_user_model
from knowledges.models import KnowledgePoint

User = get_user_model()


class Question(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    ANSWER_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]

    question_text = models.TextField()
    options = models.JSONField()  # 格式: {"A": "...", "B": "...", "C": "...", "D": "..."}
    answer = models.CharField(max_length=1, choices=ANSWER_CHOICES)
    knowledge_point = models.ForeignKey(KnowledgePoint, on_delete=models.CASCADE, related_name='questions')
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='medium')

    def __str__(self):
        return self.question_text[:50]


class Quiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quizzes', null=True, blank=True)
    questions = models.ManyToManyField(Question)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    score = models.FloatField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)  # 做题时长

    def __str__(self):
        return f'Quiz {self.id} by {self.user}'


class QuestionRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='question_records')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='records')
    selected_option = models.CharField(max_length=10)
    is_correct = models.BooleanField()
    answered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.question}'


class QuizRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quiz_records')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='records')
    score = models.FloatField()
    duration = models.DurationField()
    timestamp = models.DateTimeField(auto_now_add=True)  # 改成 timestamp，auto_now_add 保持创建时间

    def __str__(self):
        return f'{self.user} quiz {self.quiz.id} record'
