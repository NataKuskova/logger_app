from django.contrib import admin
from log_app.models import *


class LogAdmin(admin.ModelAdmin):
    list_display = ['time', 'level', 'name_logger', 'sender', 'message']
    list_display_links = ('name_logger', 'time', 'level')

admin.site.register(Log, LogAdmin)
