from django.db import models
from django.contrib.auth.models import User
from profiles.models import Station

# Create your models here.
class map(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

class TaxiCallNotification(models.Model):
    call_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Station = models.ForeignKey(Station, on_delete=models.CASCADE)



