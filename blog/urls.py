# coding:gbk
from django.urls import path
from .views import content, tags, blog_tag, about, friendly, readerWall
from . import views

urlpatterns = [
    path('<int:id>', content, name='content'),
    path('tags/', tags, name='tags'),
    path('blog_tag/<int:id>', blog_tag, name='blog_tag'),
    # path('search/', search, name='search'),
    path('about', about, name='about'),
    path('friendly', friendly, name='friendly'),
    path('readerWall', readerWall, name='readerWall'),

]
