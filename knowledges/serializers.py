from rest_framework import serializers
from .models import KnowledgePoint

class KnowledgePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnowledgePoint
        fields = '__all__'
