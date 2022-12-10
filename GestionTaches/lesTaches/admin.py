from django.contrib import admin
from datetime import datetime, timedelta, date
from lesTaches.models import Task



class TaskAdmin(admin.ModelAdmin):
    list_display=('name','description','closed','due_date','schedule_date','is_upperclass')
    read_only=('created_date')

admin.site.register(Task,TaskAdmin)