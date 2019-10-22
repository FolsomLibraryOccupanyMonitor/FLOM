from django.contrib import admin

from .models import Hour, Day, Week, Month, Year

# Register your models here.
class HourAdmin(admin.ModelAdmin):
	list_display = ('date', 'roomID', 'totalOccupants', 'avgOccLength', 'room')

class DayAdmin(admin.ModelAdmin):
	list_display = ('date', 'roomID', 'totalOccupants', 'avgOccLength', 'room')

class WeekAdmin(admin.ModelAdmin):
	list_display = ('date', 'roomID', 'totalOccupants', 'avgOccLength', 'room')

class MonthAdmin(admin.ModelAdmin):
	list_display = ('date', 'roomID', 'totalOccupants', 'avgOccLength', 'room')

class YearAdmin(admin.ModelAdmin):
	list_display = ('date', 'roomID', 'totalOccupants', 'avgOccLength', 'room')

admin.site.register(Hour, HourAdmin)
admin.site.register(Day, DayAdmin)
admin.site.register(Week, WeekAdmin)
admin.site.register(Month, MonthAdmin)
admin.site.register(Year, YearAdmin)