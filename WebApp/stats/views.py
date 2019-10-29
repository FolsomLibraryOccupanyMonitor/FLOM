from django.shortcuts import render_to_response
from stats.models import StatsLog, Hour, Day, Week, Month, Year
from datetime import datetime
from django.core.cache import cache
import time
import datetime
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
	pass
	start = datetime.datetime.now()
	lastHour = start.hour
	lastDay = start.day
	lastMonth = start.month
	lastYear = start.year

	floor3IDs = cache.get('floor3')
	floor4IDs = cache.get('floor4')
	while(True):
		time.sleep(5)
		now = datetime.datetime.now()
		if (now.hour != lastHour):
			lastHour = now.hour
			for ID in floor3IDS:
				Hour hr = new Hour()
				hr.date = now 
				hr.roomPointer = Room.objects.get(roomID=ID)
				hr.roomID = ID
				log = importLog(ID, now)
				hr.totalOccupants = log.getOccupants(roomID=ID)
				hr.avgOccLength = log.calcAvgOccLength(roomID=ID)
				hr.save()
			for ID in floor4IDs:
				Hour hr = new Hour()
				hr.date = now 
				hr.roomPointer = Room.objects.get(roomID=ID)
				hr.roomID = ID
				log = importLog(ID, now)
				hr.totalOccupants = log.getOccupants(roomID=ID)
				hr.avgOccLength = log.calcAvgOccLength(roomID=ID)
				hr.save()
		if (now.day != lastDay):
			lastDay = now.day
			for ID in floor3IDS:
				Day d = new Day()
				d.date = now 
				d.roomPointer = Room.objects.get(roomID=ID)
				d.roomID = ID
				log = importLog(ID, now)
				d.totalOccupants = log.getOccupants(roomID=ID)
				d.avgOccLength = log.calcAvgOccLength(roomID=ID)
				d.save()
			for ID in floor4IDs:
				Day d = new Day()
				d.date = now 
				d.roomPointer = Room.objects.get(roomID=ID)
				d.roomID = ID
				log = importLog(ID, now)
				d.totalOccupants = log.getOccupants(roomID=ID)
				d.avgOccLength = log.calcAvgOccLength(roomID=ID)
				d.save()
		if (now.month != lastMonth):
			lastMonth = now.month
			for ID in floor3IDS:
				Month mth = new Month()
				mth.date = now 
				mth.roomPointer = Room.objects.get(roomID=ID)
				mth.roomID = ID
				log = importLog(ID, now)
				mth.totalOccupants = log.getOccupants(roomID=ID)
				mth.avgOccLength = log.calcAvgOccLength(roomID=ID)
				mth.save()
			for ID in floor4IDs:
				Month mth = new Month()
				mth.date = now 
				mth.roomPointer = Room.objects.get(roomID=ID)
				mth.roomID = ID
				log = importLog(ID, now)
				mth.totalOccupants = log.getOccupants(roomID=ID)
				mth.avgOccLength = log.calcAvgOccLength(roomID=ID)
				mth.save()
		if (now.year != lastYear):
			lastYear = now.year
			for ID in floor3IDS:
				Year yr = new Year()
				yr.date = now 
				yr.roomPointer = Room.objects.get(roomID=ID)
				yr.roomID = ID
				log = importLog(ID, now)
				yr.totalOccupants = log.getOccupants(roomID=ID)
				yr.avgOccLength = log.calcAvgOccLength(roomID=ID)
				yr.save()
			for ID in floor4IDs:
				Year yr = new Year()
				yr.date = now 
				yr.roomPointer = Room.objects.get(roomID=ID)
				yr.roomID = ID
				log = importLog(ID, now)
				yr.totalOccupants = log.getOccupants(roomID=ID)
				yr.avgOccLength = log.calcAvgOccLength(roomID=ID)
				yr.save()		
def startThread():
	t = threading.Thread(target=threadf, args=(1,))
	t.setDaemon(True)
	t.start()

def importLog(ID, now):
	pass

def createTimeFrames(floorIDs):
	for ID in floorIDs:
		naive_datetime = datetime.datetime.now()
		curr_datetime = make_aware(naive_datetime)
		hour = Hour(date=curr_datetime, roomID=ID)
		hour.save()
		day = Day(date=curr_datetime, roomID=ID)
		day.save()
		week = Week(date=curr_datetime, roomID=ID)
		week.save()
		month = Month(date=curr_datetime, roomID=ID)
		month.save()
		year = Year(date=curr_datetime, roomID=ID)
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

def getOccupants(ID):
	'''
	Return the number of people in the room.
	Gets information from logs.
	'''
def calcAvgOccLength(ID):
	'''
	Return the average amount of time
	the room has spent occupied. 
	Gets information from logs.
	'''
