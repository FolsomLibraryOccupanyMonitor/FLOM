from django.db import models
from datetime import datetime

class Room(models.Model):
	'''
	Model for a Room
	@member (s)
		string roomID - the number of the room (ex. 301-A, 324)
		int occupied - occupation status of the room (0 = false, 1 = true)
		DateTime lastExited - date of last exit
		DateTime lastEntered - date of last entry
		string roomType - single/group designation
	'''
	roomID = models.CharField(max_length = 5) # ID of room (Ex. 301, 324)
	occupied = models.IntegerField() # 0 for empty, 1 for occupied
	lastExited = models.DateTimeField(auto_now_add=True, editable=True)
	lastEntered = models.DateTimeField(auto_now_add=True, editable=True)
	roomType = models.CharField(max_length=6) #single/group for now, could get more descriptive potentially

	def __str__(self):
		return 'Room: ' + roomID

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

	def __str__(self):
		return 'Total Occupancy: ' + str(totalOccupancy)
	
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
	occupancyStats = models.OneToOneField(OccupancyStats, on_delete=models.CASCADE)
	largestHoursInRoom = models.IntegerField()
	currentDate = models.DateTimeField(auto_now_add=True, editable=True)

	def getTimeSinceEntry(self):
		'''
		@return amount of time room has been occupied
		'''
		return datetime.now() - room.lastEntered

	def getTimeSinceExit(self):
		'''
		@return amount of time room has been empty
		'''
		return datetime.now() - room.lastExited

	def __str__(self):
		return 'Usage for ' + room.roomID