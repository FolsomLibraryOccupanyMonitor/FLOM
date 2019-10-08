from django.contrib import admin

from .models import OccupancyStats, RoomUsage
# Register your models here.

class OccupancyAdmin(admin.ModelAdmin):
	list_display = ('totalOccupancy', 'averageDayOccupancy', 'averageWeekOccupancy', 'averageMonthOccupancy')

class UsageAdmin(admin.ModelAdmin):
	list_display = ('room', 'occupancyStats', 'largestHoursInRoom', 'currentDate')

admin.site.register(OccupancyStats, OccupancyAdmin)
admin.site.register(RoomUsage, UsageAdmin)
