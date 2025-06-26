from django.contrib import admin

from .models import *

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'descrioption', 'created_at', 'published',)
    search_fields = ('title', 'descrioption')
    ordering = ('-created_at',)
