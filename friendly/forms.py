# coding:gbk
from django import forms
from .models import Friendly


class FriendlyForm(forms.ModelForm):
    class Meta:
        model = Friendly
        fields = ('website', 'url', 'content')
