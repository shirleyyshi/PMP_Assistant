from rest_framework import viewsets, filters
from .models import KnowledgePoint
from .serializers import KnowledgePointSerializer

class KnowledgePointViewSet(viewsets.ModelViewSet):
    queryset = KnowledgePoint.objects.all()
    serializer_class = KnowledgePointSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['knowledge_area', 'sub_topic', 'title']
    ordering_fields = ['created_at', 'difficulty']
    ordering = ['created_at']
