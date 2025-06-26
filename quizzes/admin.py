from django.contrib import admin
from .models import Question, Quiz, QuestionRecord, QuizRecord

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'knowledge_point', 'difficulty')
    search_fields = ('question_text',)
    list_filter = ('difficulty', 'knowledge_point')


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'completed_at', 'score')

@admin.register(QuestionRecord)
class QuestionRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'question', 'selected_option', 'is_correct', 'answered_at')

@admin.register(QuizRecord)
class QuizRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'quiz', 'score', 'duration', 'timestamp')


