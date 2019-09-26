from django.contrib import admin

from .models import OccupancyStats, RoomUsage, Room
# Register your models here.

admin.site.register(OccupancyStats)
admin.site.register(RoomUsage)
admin.site.register(Room)
