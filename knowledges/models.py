from django.db import models

class KnowledgePoint(models.Model):
    KNOWLEDGE_AREA_CHOICES = [
        ('项目整合管理', '项目整合管理'),
        ('项目范围管理', '项目范围管理'),
        ('项目进度管理', '项目进度管理'),
        ('项目成本管理', '项目成本管理'),
        ('项目质量管理', '项目质量管理'),
        ('项目资源管理', '项目资源管理'),
        ('项目沟通管理', '项目沟通管理'),
        ('项目风险管理', '项目风险管理'),
        ('项目采购管理', '项目采购管理'),
        ('项目相关方管理', '项目相关方管理'),
    ]


    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    title = models.CharField(max_length=200)  # 二级知识点标题
    content = models.TextField()
    knowledge_area = models.CharField(max_length=100, choices=KNOWLEDGE_AREA_CHOICES)
    sub_topic = models.CharField(max_length=100)  # 更精细的子分类（可用于筛选）
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.knowledge_area} - {self.title}"
