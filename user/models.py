#user/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# 장고가 관리하는 설정을 가져오기 위해 프로젝트가 아닌 django.conf 에서 settings 을 불러옴
# from mySpartaSns import settings

# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"

    bio = models.CharField(max_length=256, default='')
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followee')

