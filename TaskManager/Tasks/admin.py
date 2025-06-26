from django.contrib import admin

from .models import *

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'published',)
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
