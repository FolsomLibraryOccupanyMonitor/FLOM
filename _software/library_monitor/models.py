from django.db import models


class Log(models.Model):
    room_id = models.PositiveSmallIntegerField('room_id')
    enter_time = models.DateTimeField('enter time')
    leave_time = models.DateTimeField('leave time')
