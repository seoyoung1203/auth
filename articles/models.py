from django.db import models
from accounts.models import User
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.
class Article(models.Model): # 상속받기
    title = models.CharField(max_length=100)
    content = models.TextField()

    # 1. 직접참조
    # user = modles.ForeignKey(User, on_delete=modles.CASCADE)
    # 2. settings.py 변수 활용
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

