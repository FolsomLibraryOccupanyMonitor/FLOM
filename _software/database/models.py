from django.db import models

class RoomInfo(models.Model):
	col = models.CharField(max_length=10)