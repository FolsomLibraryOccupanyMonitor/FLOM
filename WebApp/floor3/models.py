from django.db import models

class Room(models.Model):
	'''
	Model for a Room
	@member (s)
		string roomID - the number of the room (ex. 301, 324)
		int occupied - occupation status of the room (0 = false, 1 = true)
		DateTime lastExited - date of last exit
		DateTime lastEntered - date of last entry
		string roomType - group or single room
	'''
	roomID = models.CharField(max_length = 5) # ID of room (Ex. 301, 324)
	occupied = models.IntegerField() # 0 for empty, 1 for occupied
	lastExited = models.DateTimeField()
	lastEntered = models.DateTimeField()
	roomType = models.CharField(max_length=6) #single/group for now, could get more descriptive potentially