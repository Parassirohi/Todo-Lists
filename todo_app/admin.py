from django.contrib import admin
from .models import Task, Tag
# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'due_date', 'status')
    list_filter = ('status', )
    search_fields = ('title', 'description')
    readonly_fields = ('timestamp', )
    fieldsets = (
        ('Task Details', {
            'fields': ('title', 'description', 'due_date', 'tags', 'status')
        }),
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
