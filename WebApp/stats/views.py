from django.shortcuts import render_to_response
from stats.models import StatsLog, Hour, Day, Week, Month, Year
from datetime import datetime
from django.core.cache import cache
import time
import datetime
import threading
from floor.models import Room
from django.utils.timezone import make_aware

def index(request):
	'''
	@return display of stats page
	'''
	return render_to_response('stats/templates/html/stats.html')

def log(rID, e):
	currLog = StatsLog(event = e, roomID = rID)
	currLog.save()

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
	while(True):
		time.sleep(5)
		print("Here")
		now = datetime.datetime.now()
		if (now.hour != lastHour):
			lastHour = now.hour
			for ID in floor3IDs:
				hr = Hour()
				hr.date = now 
				hr.roomPointer = Room.objects.get(roomID=ID)
				hr.roomID = ID
				logList = importLog(ID, now)
				hr.totalOccupants = getOccupants(logList, ID)
				hr.avgOccLength = calcAvgOccLength(logList, ID)
				hr.save()
			for ID in floor4IDs:
				hr = Hour()
				hr.date = now 
				hr.roomPointer = Room.objects.get(roomID=ID)
				hr.roomID = ID
				logList = importLog(ID, now)
				hr.totalOccupants = getOccupants(logList, ID)
				hr.avgOccLength = calcAvgOccLength(logList, ID)
				hr.save()
		if (now.day != lastDay):
			lastDay = now.day
			for ID in floor3IDs:
				d = Day()
				d.date = now 
				d.roomPointer = Room.objects.get(roomID=ID)
				d.roomID = ID
				logList = importLog(ID, now)
				d.totalOccupants = getOccupants(logList, ID)
				d.avgOccLength = calcAvgOccLength(logList, ID)
				d.save()
			for ID in floor4IDs:
				d = Day()
				d.date = now 
				d.roomPointer = Room.objects.get(roomID=ID)
				d.roomID = ID
				logList = importLog(ID, now)
				d.totalOccupants = getOccupants(logList, ID)
				d.avgOccLength = calcAvgOccLength(logList, ID)
				d.save()
		if (now.month != lastMonth):
			lastMonth = now.month
			for ID in floor3IDs:
				mth = Month()
				mth.date = now 
				mth.roomPointer = Room.objects.get(roomID=ID)
				mth.roomID = ID
				logList = importLog(ID, now)
				mth.totalOccupants = getOccupants(logList, ID)
				mth.avgOccLength = calcAvgOccLength(logList, ID)
				mth.save()
			for ID in floor4IDs:
				mth = Month()
				mth.date = now 
				mth.roomPointer = Room.objects.get(roomID=ID)
				mth.roomID = ID
				logList = importLog(ID, now)
				mth.totalOccupants = getOccupants(logList, ID)
				mth.avgOccLength = calcAvgOccLength(logList, ID)
				mth.save()
		if (now.year != lastYear):
			lastYear = now.year
			for ID in floor3IDs:
				yr = Year()
				yr.date = now 
				yr.roomPointer = Room.objects.get(roomID=ID)
				yr.roomID = ID
				logList = importLog(ID, now)
				yr.totalOccupants = getOccupants(logList, ID)
				yr.avgOccLength = calcAvgOccLength(logList, ID)
				yr.save()
			for ID in floor4IDs:
				yr = Year()
				yr.date = now 
				yr.roomPointer = Room.objects.get(logList, ID)
				yr.roomID = ID
				logList = importLog(ID, now)
				yr.totalOccupants = getOccupants(logList, ID)
				yr.avgOccLength = calcAvgOccLength(logList, ID)
				yr.save()		
def startThread():
	print("Starting Thread")
	t = threading.Thread(target=threadf, args=(1,))
	t.setDaemon(True)
	t.start()

def importLog(ID, now):
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
