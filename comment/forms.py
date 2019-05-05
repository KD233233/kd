# coding:gbk
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  # 表明这个表单对应的数据库模型是Comment类
        fields = ['name', 'email', 'content']  # 指定了表单要显示的字段
