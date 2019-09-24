from django.db import models

# Create your models here.
class Room(models.Model):
	roomID = models.CharField(max_length = 5) # ID of room (Ex. 301, 324)
	occupied = models.IntegerField() # 0 for empty, 1 for occupied
	lastExited = models.DateTimeField()
	lastEntered = models.DateTimeField()