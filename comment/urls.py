#coding:gbk
from django.urls import path
from .views import post_comment


urlpatterns = [
    path('comment/post/<int:post_id>', post_comment, name='post_comment'),

]
