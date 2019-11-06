from django.contrib import admin

from .models import OccupancyStats, RoomUsage, Room
# Register your models here.

class OccupancyAdmin(admin.ModelAdmin):
	list_display = ('totalOccupancy', 'averageDayOccupancy', 'averageWeekOccupancy', 'averageMonthOccupancy')

class UsageAdmin(admin.ModelAdmin):
	list_display = ('room', 'occupancyStats', 'largestHoursInRoom', 'currentDate')

class RoomAdmin(admin.ModelAdmin):
	list_display = ('roomID', 'occupied', 'lastEntered', 'lastExited', 'roomType')

admin.site.register(OccupancyStats, OccupancyAdmin)
admin.site.register(RoomUsage, UsageAdmin)
admin.site.register(Room, RoomAdmin)
