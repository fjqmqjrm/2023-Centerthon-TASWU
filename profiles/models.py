# profiles/models.py

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # null=True를 설정하여 UserProfile과 User의 1대1 관계에서 UserProfile이 없어도 됨을 나타냄
    # 여기에 원하는 추가 정보 필드들을 정의합니다
    # 예를 들어, 닉네임, 프로필 사진, 연락처 등
    image = models.ImageField(blank=True, null=True, upload_to='static/img/profile')
    phone_number = models.CharField(null=True, max_length=20)
    coins = models.PositiveIntegerField(default=4, null=True)

    is_taxi_driver = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
    
    
class Station(models.Model):
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200, null=True)
    UserProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)

class TaxiCall(models.Model): #누가 어디서 호출했는지 택시 호출 여부를 판단 & 기사님이 생기면 수락으로 판단
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE,related_name='taxi_calls_as_client')
    driver = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, related_name='taxi_calls_as_driver')
    address = models.CharField(max_length=200)
