from django import forms
from django.utils import timezone

from .models import Diary

class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ('title', 'description', 'time', 'image')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 타임 필드에 현재 시간을 기본값으로 설정
        self.fields['time'].initial = timezone.now()