from django.contrib import admin
from .models import Friendly


# Register your models here.

@admin.register(Friendly)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('website', 'id', 'url', 'content')
