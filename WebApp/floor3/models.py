from django.db import models

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