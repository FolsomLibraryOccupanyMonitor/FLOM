from django.contrib import admin

from .models import StatsLog
# Register your models here.

class StatsLogAdmin(admin.ModelAdmin):
	list_display = ('roomPointer', 'event','roomID','timeStamp')

admin.site.register(StatsLog, StatsLogAdmin)
