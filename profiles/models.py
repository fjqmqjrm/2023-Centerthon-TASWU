# profiles/models.py

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # null=True를 설정하여 UserProfile과 User의 1대1 관계에서 UserProfile이 없어도 됨을 나타냄
    # 여기에 원하는 추가 정보 필드들을 정의합니다
    # 예를 들어, 닉네임, 프로필 사진, 연락처 등
    nickname = models.CharField(null=True,default="닉네임", max_length=20)
    email = models.EmailField(null=True)
    image = models.ImageField(blank=True, null=True, upload_to='static/img/profile')
    phone_number = models.CharField(null=True, max_length=20)
    current_location = models.CharField(null=True, max_length=200)   

    is_taxi_driver = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
    
    
class Station(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    UserProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)

# class TaxiCallNotification(models.Model):
#     call_id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     Station = models.ForeignKey(Station, on_delete=models.CASCADE)



