from django.db import models


# Create your models here.
class Room(models.Model):
    room_id = models.IntegerField()
    key = models.CharField(max_length=200)


class Occupancy(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    occupied = models.BooleanField()

