from django.db import models

class Room(models.Model):
	room_name = models.CharField('Room Name', max_length=20, null = True, default = "", editable = False)
	room_floor = models.CharField('Room floor', max_length=20, null = True, default = "", editable = False)

class Log(models.Model):
	room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
	enter_time = models.DateTimeField('Enter Time')
	leave_time = models.DateTimeField('Leave Time')

class Occupy(models.Model):
	room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
	time = models.DateTimeField('Time')