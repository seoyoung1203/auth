from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass
# Django의 기본 User 모델(auth.User)이 동시에 존재하기 때문에 충돌 발생