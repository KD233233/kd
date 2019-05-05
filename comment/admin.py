from django.contrib import admin
from .models import Comment

# Register your models here.

@admin.register(Comment)
class commentAdmin(admin.ModelAdmin):
    list_display = ('name','email','content','time')