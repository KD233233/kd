# coding:gbk
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  # �����������Ӧ�����ݿ�ģ����Comment��
        fields = ['name', 'email', 'content']  # ָ���˱�Ҫ��ʾ���ֶ�
