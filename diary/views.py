from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from requests import Response
from rest_framework.decorators import api_view

from accounts.models import User
from .forms import DiaryForm
from .models import Diary

# Create your views here.

#유저
@login_required
def user_info(request):
    userinfo = User.objects.all()
    return render(request, 'diary/mainIndex.html', {'userinfo' : userinfo })

#다이어리
def diary_list(request):
    return render(request, 'diary/mainIndex.html', )

#작성
def diary_post(request):
    if request.method == "POST":
        form = DiaryForm(request.POST)

        if form.is_valid():
            diary = form.save(commit=False)
            diary.save()
            return redirect('diary_list')

    else:
        form = DiaryForm()

    return render(request, 'diary/paragraphindex.html', {'form' : form})