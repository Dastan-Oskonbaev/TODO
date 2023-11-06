from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'description',
        'created',
        'completed',
    ]
    list_filter = [
        'title',
    ]
    search_fields = [
        'title',
    ]
    ordering = [
        'title',
    ]
    readonly_fields = [
        'created',
    ]
    save_on_top = True
