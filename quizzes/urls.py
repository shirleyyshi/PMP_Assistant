from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import QuestionViewSet, QuizViewSet, QuestionRecordViewSet, QuizRecordViewSet

router = DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'quizzes', QuizViewSet)
router.register(r'question-records', QuestionRecordViewSet, basename='questionrecord')
router.register(r'quiz-records', QuizRecordViewSet, basename='quizrecord')

urlpatterns = [
    path('', include(router.urls)),
]
