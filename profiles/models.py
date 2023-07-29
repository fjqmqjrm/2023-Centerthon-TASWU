# profiles/models.py

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # null=True를 설정하여 UserProfile과 User의 1대1 관계에서 UserProfile이 없어도 됨을 나타냄
    # 여기에 원하는 추가 정보 필드들을 정의합니다
    # 예를 들어, 닉네임, 프로필 사진, 연락처 등
    is_taxi_driver = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username