from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('assistant', 'Assistant'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    progress = models.JSONField(
        default=dict,
        blank=True,
        null=True,
        help_text="仅对 student 用户生效，用于记录学习进度"
    )

    def save(self, *args, **kwargs):
        # 若为 assistant，则清空 progress 字段
        if self.role == 'assistant':
            self.progress = None
        elif self.progress is None:
            self.progress = {}
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} ({self.role})"

