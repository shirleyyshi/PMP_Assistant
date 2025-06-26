from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KnowledgePointViewSet

router = DefaultRouter()
router.register(r'knowledgepoints', KnowledgePointViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
