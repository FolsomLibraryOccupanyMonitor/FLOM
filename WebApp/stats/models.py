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



# class OccupancyStats(models.Model):
# 	'''
# 	Contains useful occupancy statistics
# 	@member (s)
# 		totalOccupancy - the total number of occupants since program launch
# 		averageDayOccupancy - average number of occupants for each day
# 		averageWeekOccupancy - average number of occupants for each week
# 		averageMonthOccupancy - average number of occupants for each month
# 	'''
# 	totalOccupancy = models.IntegerField(default = 0)
# 	averageDayOccupancy = models.IntegerField(default = 0)
# 	averageWeekOccupancy = models.IntegerField(default = 0)
# 	averageMonthOccupancy = models.IntegerField(default = 0)
	
# class RoomUsage(models.Model):
# 	'''
# 	Model for holding statistics about room usage
# 	@member (s)
# 		room - uses Room model for room information
# 		occupancy_stats - uses OccupancyStats model for useful fields for stats
# 		largestHoursInRoom - the "high score" for most time spent in the room
# 		currentDate - holds the current date and time for the room
# 	'''
# 	room = models.OneToOneField(Room, on_delete=models.CASCADE)
# 	occupancyStats = models.OneToOneField(OccupancyStats, on_delete=models.CASCADE)
# 	largestHoursInRoom = models.IntegerField(default=0)
# 	currentDate = models.DateTimeField(auto_now_add=True, editable=True)
