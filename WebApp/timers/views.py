from django.shortcuts import render
import threading
import time
import datetime
from .models import Hour, Day, Week, Month, Year
from floor.models import Room
from django.core.cache import cache
from django.utils.timezone import make_aware
# Create your views here.


def index(request):
	'''
	@return display of stats page
	'''
	print("STATS")

def threadf(name):
	start = datetime.datetime.now()
	lastHour = start.hour
	lastDay = start.day
	# lastWeek = start.week
	lastMonth = start.month
	lastYear = start.year
	while(True):
		time.sleep(5)
		now = datetime.datetime.now()
		if (now.hour != lastHour):
			lastHour = now.hour
			print("An hour has passed")
		if (now.day != lastDay):
			lastDay = now.day
			print("An day has passed")
		if (now.month != lastMonth):
			lastMonth = now.month
			print("An hour has passed")
		if (now.year != lastYear):
			lastYear = now.year
			print("An hour has passed")
		

def startThread():
	t = threading.Thread(target=threadf, args=(1,))
	t.setDaemon(True)
	t.start()

def createTimeFrames(floorIDs):
	for ID in floorIDs:
		room_query = Room.objects.filter(roomID=ID)[0]
		naive_datetime = datetime.datetime.now()
		curr_datetime = make_aware(naive_datetime)
		hour = Hour(date=curr_datetime, room=room_query, roomID=ID)
		hour.save()
		day = Day(date=curr_datetime, room=room_query, roomID=ID)
		day.save()
		week = Week(date=curr_datetime, room=room_query, roomID=ID)
		week.save()
		month = Month(date=curr_datetime, room=room_query, roomID=ID)
		month.save()
		year = Year(date=curr_datetime, room=room_query, roomID=ID)
		year.save()

def initializeData():
	'''
	Initialize database with start
	day, week, month, and year
	Should only be called once at startup
	'''
	floor3IDs = cache.get('floor3')
	floor4IDs = cache.get('floor4')
	createTimeFrames(floor3IDs)
	createTimeFrames(floor4IDs)

