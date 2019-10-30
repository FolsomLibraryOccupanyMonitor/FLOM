from django.shortcuts import render_to_response
from stats.models import StatsLog, Hour, Day, Week, Month, Year
from datetime import datetime
from django.core.cache import cache
import time
import datetime
import threading
from floor.models import Room

def index(request):
	'''
	@return display of stats page
	'''
	return render_to_response('stats/templates/html/stats.html')

def log(rID, e):
	currLog = StatsLog(event = e, roomID = rID)
	currLog.save()


def createTimeObject(ID, duration, now):
	timeObject = None
	if(duration == "hour"):
		timeObject = Hour()
	elif(duration == "day"):
		timeObject = Day()
	elif(duration == "month"):
		timeObject = Month()
	elif(duration == "year"):
		timeObject = Year()
	else:
		print("ERROR: INVALID TIME OBJECT REQUEST")
	timeObject.date = now 
	timeObject.roomPointer = Room.objects.get(roomID=ID)
	timeObject.roomID = ID
	logList = importLog(ID, now, duration)
	timeObject.totalOccupants = getOccupants(logList, ID)
	timeObject.avgOccLength = calcAvgOccLength(logList, ID)
	timeObject.save()


def threadf(name):
	''''''
	#Seperate thread which creates time objects
	#every hour/day/month/year. Everytime one of 
	#those pass create an object with information
	#from logs for each room 
	''''''
	start = datetime.datetime.now()
	lastHour = start.hour
	lastDay = start.day
	lastMonth = start.month
	lastYear = start.year

	floor3IDs = cache.get('floor3')
	floor4IDs = cache.get('floor4')
	now = datetime.datetime.now()
	while(True):
		time.sleep(5)
		now = datetime.datetime.now()
		if (now.hour != lastHour):
			lastHour = now.hour
			for ID in floor3IDs:
				createTimeObject(ID,"hour",now)
			for ID in floor4IDs:
				createTimeObject(ID,"hour",now)
		if (now.day != lastDay):
			lastDay = now.day
			for ID in floor3IDs:
				createTimeObject(ID,"day",now)
			for ID in floor4IDs:
				createTimeObject(ID,"day",now)
		if (now.month != lastMonth):
			lastMonth = now.month
			for ID in floor3IDs:
				createTimeObject(ID,"month",now)				
			for ID in floor4IDs:
				createTimeObject(ID,"month",now)
		if (now.year != lastYear):
			lastYear = now.year
			for ID in floor3IDs:
				createTimeObject(ID,"year",now)
			for ID in floor4IDs:
				createTimeObject(ID,"year",n)	
def startThread():
	print("Starting Thread")
	t = threading.Thread(target=threadf, args=(1,))
	t.setDaemon(True)
	t.start()

def importLog(ID, now, duration):
	return 1


def getOccupants(logList, ID):
	'''
	Return the number of people in the room.
	Gets information from logs.
	'''
	return 1
def calcAvgOccLength(logList, ID):
	'''
	Return the average amount of time
	the room has spent occupied. 
	Gets information from logs.
	'''
	return 1
