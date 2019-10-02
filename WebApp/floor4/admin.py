from django.contrib import admin

from floor4.models import Room

class RoomAdmin(admin.ModelAdmin):
	'''
	Model for RoomAdmin
	'''
	list_display = ('roomID', 'occupied', 'lastEntered', 'lastExited', 'roomType')

admin.site.register(Room, RoomAdmin)