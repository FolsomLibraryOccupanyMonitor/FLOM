from django.contrib import admin

from .models import StatsLog, Hour, Day, Week, Month, Year
# Register your models here.

class StatsLogAdmin(admin.ModelAdmin):
	list_display = ('roomID', 'event', 'timeStamp')

class HourAdmin(admin.ModelAdmin):
	list_display = ('date', 'roomID', 'totalOccupants', 'avgOccLength')

class DayAdmin(admin.ModelAdmin):
	list_display = ('date', 'roomID', 'totalOccupants', 'avgOccLength')

class WeekAdmin(admin.ModelAdmin):
	list_display = ('date', 'roomID', 'totalOccupants', 'avgOccLength')

class MonthAdmin(admin.ModelAdmin):
	list_display = ('date', 'roomID', 'totalOccupants', 'avgOccLength')

class YearAdmin(admin.ModelAdmin):
	list_display = ('date', 'roomID', 'totalOccupants', 'avgOccLength')

admin.site.register(StatsLog, StatsLogAdmin)
admin.site.register(Hour, HourAdmin)
admin.site.register(Day, DayAdmin)
admin.site.register(Week, WeekAdmin)
admin.site.register(Month, MonthAdmin)
admin.site.register(Year, YearAdmin)