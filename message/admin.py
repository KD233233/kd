from django.contrib import admin
from .models import Message

# Register your models here.
@admin.register(Message)
class messageAdmin(admin.ModelAdmin):
    list_display = ('name','email','content','time')
