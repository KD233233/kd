#coding:gbk
from django.urls import path
from .views import about_message


urlpatterns = [
    path('message/post', about_message, name='about_message'),
]