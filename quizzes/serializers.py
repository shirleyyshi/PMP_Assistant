from rest_framework import serializers
from .models import Question, Quiz, QuestionRecord, QuizRecord
from knowledges.serializers import KnowledgePointSerializer


class QuestionSerializer(serializers.ModelSerializer):
    knowledge_point = KnowledgePointSerializer(read_only=True)
    knowledge_point_id = serializers.PrimaryKeyRelatedField(
        queryset=KnowledgePointSerializer.Meta.model.objects.all(),
        source='knowledge_point',
        write_only=True
    )

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'options', 'answer', 'difficulty', 'knowledge_point', 'knowledge_point_id']


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ['id', 'user', 'questions', 'created_at', 'completed_at', 'score', 'duration']


class QuestionRecordSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(read_only=True)

    class Meta:
        model = QuestionRecord
        fields = ['id', 'user', 'question', 'selected_option', 'is_correct', 'answered_at']


class QuizRecordSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer(read_only=True)

    class Meta:
        model = QuizRecord
        fields = ['id', 'user', 'quiz', 'score', 'duration', 'timestamp']
