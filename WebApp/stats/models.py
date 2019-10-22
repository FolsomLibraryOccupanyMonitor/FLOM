from django.db import models
from datetime import datetime

from floor.models import Room

class statsLog(models.Model):
	'''
	Contains useful occupancy statistics
	@member (s)
		room - Room for which the logs are stored for
		event - enter/exit-1/0
		roomID = room ID of room
		timeStamp - exact date time of the log
	'''
	roomPointer = models.ForeignKey(Room, on_delete=models.CASCADE)
	event = models.IntegerField(default = 0)
	roomID = models.CharField(max_length = 5)
	timeStamp = models.DateTimeField(auto_now_add=True, editable=False)

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
	date = models.DateField(auto_now_add=True, editable=False)
	roomPointer = models.ForeignKey(Room, on_delete=models.CASCADE)
	span = models.CharField(max_length=6)
	roomID = models.CharField(max_length=5)
	totalOccupants = models.IntegerField(default=0)
	avgOccLength = models.IntegerField(default=0)