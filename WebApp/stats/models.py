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







class Room(models.Model):
	'''
	Model for a Room
	@member (s)
		int roomID - the number of the room (ex. 301, 324)
		int occupied - occupation status of the room (0 = false, 1 = true)
		Date lastExited - date of last exit
		Date lastEntered - date of last entry
	'''
	roomID = models.CharField(max_length = 5) # ID of room (Ex. 301, 324)
	occupied = models.IntegerField() # 0 for empty, 1 for occupied
	lastExited = models.DateTimeField()
	lastEntered = models.DateTimeField()
	roomType = models.CharField() #single/group for now, could get more descriptive potentially
