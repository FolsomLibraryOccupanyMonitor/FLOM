from django.contrib import admin

from .models import StatsLog
# Register your models here.

class StatsLogAdmin(admin.ModelAdmin):
	list_display = ('roomID', 'event', 'timeStamp')

admin.site.register(StatsLog, StatsLogAdmin)
