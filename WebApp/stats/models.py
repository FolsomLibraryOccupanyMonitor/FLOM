from django.db import models
from datetime import datetime

class OccupancyStats(models.Model):
	'''
	Contains useful occupancy statistics
	@member (s)
		totalOccupancy - the total number of occupants since program launch
		averageDayOccupancy - average number of occupants for each day
		averageWeekOccupancy - average number of occupants for each week
		averageMonthOccupancy - average number of occupants for each month
	'''
	totalOccupancy = models.IntegerField()
	averageDayOccupancy = models.IntegerField()
	averageWeekOccupancy = models.IntegerField()
	averageMonthOccupancy = models.IntegerField()
	currentOccupancyTime = models.DateTimeField()
	
class RoomUsage(models.Model):
	'''
	Model for holding statistics about room usage
	@member (s)
		room - uses Room model for room information
		occupancy_stats - uses OccupancyStats model for useful fields for stats
		largestHoursInRoom - the "high score" for most time spent in the room
		currentDate - holds the current date and time for the room
	'''
	room = models.OneToOneField(Room, on_delete=models.CASCADE)
	occupancy_stats = models.OneToOneField(OccupancyStats, on_delete=models.CASCADE)
	largestHoursInRoom = models.IntegerField()
	currentDate = models.DateTimeField()






