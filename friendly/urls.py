#coding:gbk
from django.urls import path
from .views import friendly_link


urlpatterns = [
    path('friendly/post', friendly_link, name='friendly_link'),
]