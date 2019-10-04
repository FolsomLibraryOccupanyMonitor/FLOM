from django.contrib import admin

from .models import Floor

class FloorAdmin(admin.ModelAdmin):
	'''
	Model for displaying info on admin page for Floor model
	'''
	list_display = ('floor')
	
admin.site.register(Floor, FloorAdmin)