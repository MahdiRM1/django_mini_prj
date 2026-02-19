from django.contrib import admin
from django.contrib.admin import register

from tasks.models import *

@register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'is_done', 'priority', 'due_date', 'created_at']
    list_editable = ['is_done']
    list_filter = ['is_done', 'priority']
    search_fields = ['title']
    list_display_links = ['title']
    list_per_page = 20
    sortable_by = ['title', 'created_at', 'id', 'priority']

admin.site.register(Tag)