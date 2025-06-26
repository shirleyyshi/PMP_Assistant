from django.contrib import admin
from .models import User  # 如果你自定义了User模型

admin.site.register(User)

