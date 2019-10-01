from django.db import models

# Create your models here.
class Room(models.Model):
	roomID = models.CharField(max_length = 5) # ID of room (Ex. 301, 324)
	occupied = models.IntegerField() # 0 for empty, 1 for occupied
	lastExited = models.DateField()
	lastEntered = models.DateField()
	roomType = models.CharField(max_length=6, default='S') #single/group for now, could get more descriptive potentially