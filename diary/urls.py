from django.urls import path
from . import views

app_name = 'diary'

urlpatterns = [
    path('main/', views.diary_list, name='diary_list'),
    path('post/', views.diary_post, name='diary_post'),
]