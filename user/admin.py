# 장고의 어드민 페이지 사용
from django.contrib import admin
# 본 파일의 models.py 파일에 접근하여 UserModel 클래스를 가져온다.
from .models import UserModel

# Register your models here.
# 이 코드가 나의 UserModel을 Admin에 추가 해 줍니다
admin.site.register(UserModel)