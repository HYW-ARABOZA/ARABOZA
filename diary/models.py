from django.db import models
from accounts.models import UserManager


# Create your models here.

#일기
class Diary(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(blank=False)
    time = models.DateTimeField(blank=True)
    weather = models.TextField(max_length=100)

    def __str__(self):
        return self.title

    def get_diary_content(self):
        return f"Title: {self.title}\nDescription: {self.description}\nTime: {self.time}\nWeather: {self.weather}"