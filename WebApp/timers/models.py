from django.db import models
from floor.models import Room

'''
	These models are a representation of the usage statistics that have
	been gathered within the span of the designated time.
	@member (s)
		date - date on which TimeFrame was created
		room - points to the room it refers to
		roomID - individual room this applies to
		totalOccupants - total number of occupants over the span
		avgOccLength - average occupation length for a room (in minutes)
'''

class Hour(models.Model):
	date = models.DateTimeField()
	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	roomID = models.CharField(max_length=5)
	totalOccupants = models.IntegerField(default=0)
	avgOccLength = models.IntegerField(default=0)

class Day(models.Model):
	date = models.DateTimeField()
	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	roomID = models.CharField(max_length=5)
	totalOccupants = models.IntegerField(default=0)
	avgOccLength = models.IntegerField(default=0)

class Week(models.Model):
	date = models.DateTimeField()
	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	roomID = models.CharField(max_length=5)
	totalOccupants = models.IntegerField(default=0)
	avgOccLength = models.IntegerField(default=0)

class Month(models.Model):
	date = models.DateTimeField()
	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	roomID = models.CharField(max_length=5)
	totalOccupants = models.IntegerField(default=0)
	avgOccLength = models.IntegerField(default=0)

class Year(models.Model):
	date = models.DateTimeField()
	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	roomID = models.CharField(max_length=5)
	totalOccupants = models.IntegerField(default=0)
	avgOccLength = models.IntegerField(default=0)