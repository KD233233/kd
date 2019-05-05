from django.contrib import admin
from .models import Sentence, Tags, Post, ReadNum, About


# Register your models here.


@admin.register(Sentence)
class SentenceAdmin(admin.ModelAdmin):
    list_display = ('time', 'content', 'id')


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'pub_time', 'classify', 'author', 'readnum', 'zan', 'adv', 'img',)


@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ('look', 'post')


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('content', 'qq', 'group', 'email')
