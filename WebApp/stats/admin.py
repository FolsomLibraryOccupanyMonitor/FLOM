from django.contrib import admin

from .models import statsLog
# Register your models here.

class statsLogAdmin(admin.ModelAdmin):
	list_display = ('roomPointer', 'event','roomID','timeStamp')

admin.site.register(statsLog,statsLogAdmin)
