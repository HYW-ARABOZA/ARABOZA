from django.db import models
from django.utils import timezone
from django.utils.datetime_safe import datetime

from accounts.models import UserManager


# Create your models here.

#일기
class Diary(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(blank=False)
    time = models.DateTimeField(default= models.DateTimeField(auto_now_add=True)) #현재 시간을 자동으로
    #날짜만 자동으로 저장하게 하는 방법은 없을까효
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title

    def get_diary_content(self):
        return f"Title: {self.title}\nDescription: {self.description}\nTime: {self.time}\nWeather: {self.weather}"