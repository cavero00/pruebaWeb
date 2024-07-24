from django.contrib import admin
from .models import *

class TaskAdmin(admin.ModelAdmin):
    list_display =  ["title", "user", "created", "datecompleted", "imporant"]
    readonly_fields = ["created",]

# Register your models here.
admin.site.register(Task, TaskAdmin)