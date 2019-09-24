from django.contrib import admin

from floor3.models import Room

class RoomAdmin(admin.ModelAdmin):
	'''
	Model for a RoomAdmin
	'''
	list_display = ('roomID', 'occupied', 'lastEntered', 'lastExited')

admin.site.register(Room, RoomAdmin)