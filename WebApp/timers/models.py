from django.db import models
from floor.models import Room
# Create your models here.
class TimeFrame(models.Model):
	'''
	A TimeFrame is a representation of the usage statistics that have
	been gathered within the span of the designated time.
	@member (s)
		date - date on which TimeFrame was created
		span - interval in which the statistics were gathered
				eg. "day", "week", "month", "year"
		roomID - individual room this applies to
		totalOccupants - total number of occupants over the span
		avgOccLength - average occupation length for a room (in minutes)
	'''
	date = models.DateField()
	roomPointer = models.ForeignKey(Room, on_delete=models.CASCADE)
	span = models.CharField(max_length=6)
	roomID = models.CharField(max_length=5)
	totalOccupants = models.IntegerField(default=0)
	avgOccLength = models.IntegerField(default=0)