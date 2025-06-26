from rest_framework import viewsets
from .models import AssistantLog
from .serializers import AssistantLogSerializer

class AssistantLogViewSet(viewsets.ModelViewSet):
    queryset = AssistantLog.objects.all()
    serializer_class = AssistantLogSerializer

