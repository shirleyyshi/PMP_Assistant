from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AssistantLogViewSet

router = DefaultRouter()
router.register(r'assistantlogs', AssistantLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
