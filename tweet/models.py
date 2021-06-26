# tweet/models.py
from django.db import models
# user 앱의 model을 가져오고 UserModel 클래스를 가져온다.
from user.models import UserModel
from taggit.managers import TaggableManager

# Create your models here.
class TweetModel(models.Model):
    class Meta:
        db_table = "tweet"
    # 다른 모델을 가져와서 넣어놓겠다.
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=256)
    tags = TaggableManager(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TweetComment(models.Model):
    class Meta:
        db_table = "comment"

    tweet = models.ForeignKey(TweetModel, on_delete=models.CASCADE)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    comment = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)