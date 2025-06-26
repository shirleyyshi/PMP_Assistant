from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Question, Quiz, QuestionRecord, QuizRecord
from .serializers import QuestionSerializer, QuizSerializer, QuestionRecordSerializer, QuizRecordSerializer
from django.contrib.auth import get_user_model
from django.utils import timezone
from random import sample

User = get_user_model()

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['post'], url_path='generate')
    def generate_quiz(self, request):
        """
        用户选择题目数量和知识点范围，随机组卷
        请求体示例:
        {
            "num_questions": 10,
            "knowledge_point_ids": [1,2,3]
        }
        """
        num_questions = request.data.get('num_questions')
        knowledge_point_ids = request.data.get('knowledge_point_ids', [])

        if not num_questions or int(num_questions) <= 0:
            return Response({'detail': 'num_questions 必须是正整数'}, status=status.HTTP_400_BAD_REQUEST)

        questions_qs = Question.objects.filter(knowledge_point_id__in=knowledge_point_ids)
        total = questions_qs.count()
        if total < int(num_questions):
            return Response({'detail': '题库中题目数量不足'}, status=status.HTTP_400_BAD_REQUEST)

        selected_questions = sample(list(questions_qs), int(num_questions))

        quiz = Quiz.objects.create(user=request.user)
        quiz.questions.set(selected_questions)
        quiz.save()

        serializer = self.get_serializer(quiz)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], url_path='submit')
    def submit_quiz(self, request, pk=None):
        """
        提交组卷结果，包含每道题用户选择和对错，计算分数和时长
        请求体示例:
        {
            "answers": [
                {"question_id": 1, "selected_option": "A"},
                {"question_id": 2, "selected_option": "C"},
                ...
            ],
            "duration_seconds": 600
        }
        """
        quiz = self.get_object()
        answers = request.data.get('answers', [])
        duration_seconds = request.data.get('duration_seconds', 0)

        correct_count = 0
        total_questions = quiz.questions.count()

        for ans in answers:
            question_id = ans.get('question_id')
            selected_option = ans.get('selected_option')

            try:
                question = Question.objects.get(id=question_id)
            except Question.DoesNotExist:
                continue

            is_correct = (selected_option == question.answer)
            if is_correct:
                correct_count += 1

            # 记录 QuestionRecord
            QuestionRecord.objects.create(
                user=request.user,
                question=question,
                selected_option=selected_option,
                is_correct=is_correct
            )

        score = (correct_count / total_questions * 100) if total_questions > 0 else 0
        quiz.score = score
        quiz.duration = timezone.timedelta(seconds=duration_seconds)
        quiz.completed_at = timezone.now()
        quiz.save()

        # 记录 QuizRecord
        QuizRecord.objects.create(
            user=request.user,
            quiz=quiz,
            score=score,
            duration=quiz.duration
        )

        serializer = self.get_serializer(quiz)
        return Response(serializer.data)


class QuestionRecordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = QuestionRecord.objects.all()
    serializer_class = QuestionRecordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # 只返回当前登录用户的答题记录
        return self.queryset.filter(user=self.request.user)


class QuizRecordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = QuizRecord.objects.all()
    serializer_class = QuizRecordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # 只返回当前登录用户的测验记录
        return self.queryset.filter(user=self.request.user)
