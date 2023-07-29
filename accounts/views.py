from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.response import Response
from uuid import uuid4
import os

from .models import User
from project.settings import MEDIA_ROOT

# 회원가입
class Join(APIView):
    def get(self, request):
        return render(request, 'accounts/join.html')

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        nickname = request.data.get('nickname')
        password = request.data.get('password')

        if User.objects.filter(email=email).exists():
            return Response(status=500, data=dict(message='해당 이메일주소는 이미 사용중입니다.'))
        elif User.objects.filter(nickname=nickname).exists():
            return Response(status=500, data=dict(message='닉네임 "' + nickname + '"이(가) 이미 존재합니다.'))

        User.objects.create(password=make_password(password), email=email, nickname=nickname, username=username)

        return Response(status=200, data=dict(message='회원가입 성공!'))

# 로그인

@login_required
class Login(APIView):
    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        if email is None:
            return Response(status=500, data=dict(message='이메일을 입력해주세요'))

        if password is None:
            return Response(status=500, data=dict(message='비밀번호를 입력해주세요'))

        user = User.objects.filter(email=email).first()

        if user is None:
            return Response(status=500, data=dict(messag='입력정보가 올바르지않습니다.'))

        if check_password(password, user.password) is False:
            return Response(status=500, data=dict(message='비밀번호가 올바르지 않습니다.'))

        request.session['loginCheck'] = True
        request.session['email'] = user.email

        return Response(status=200, data=dict(message='로그인 성공!'))


@login_required
def login(request):
    if request.method == "GET":
        return render(request, 'accounts/login.html')

    elif request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        if email is None:
            return Response(status=500, data=dict(message='이메일을 입력해주세요'))

        if password is None:
            return Response(status=500, data=dict(message='비밀번호를 입력해주세요'))

        user = authenticate(request, email=email, password=password)

        if user is not None:
            request.session['loginCheck'] = True
            request.session['email'] = user.email
            login(request, user)
            return render(request, 'diary/mainIndex.html', context='로그인 성공!')

        elif user is None:
            return Response(status=500, data=dict(messag='입력정보가 올바르지 않습니다.'))

        elif check_password(password, user.password) is False:
            return Response(status=500, data=dict(message='비밀번호가 올바르지 않습니다.'))

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')




