from django.shortcuts import render_to_response
from stats.models import StatsLog, Day,  Month, Year
from django.http import HttpResponse
from datetime import datetime
from django.core.cache import cache
import time
import datetime
import threading
from floor.models import Room
from django.db.models import Sum, Avg, F
from django.contrib.auth.decorators import login_required


def render_statistics(request, duration):
	stats = {}
	available_stats = []
	titles = ['roomID', 'date', 'totalOccupants', 'avgOccLength']
	query = None
	if duration == 'day':
		query = Day.objects.all();
	elif duration == 'month':
		query = Month.objects.all();
	else:
		query = Year.objects.all();
	for obj in query:
		for title in titles:
			available_stats.append({title:getattr(obj, title)})
	stats['stats'] = available_stats
	print(stats)
	display = render_to_response('stats/templates/html/stats.html', stats)
	return display

@login_required
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
	if duration == "day":
		timeObject = Day()
	elif duration == "month":
		timeObject = Month()
	elif duration == "year":
		timeObject = Year()
	else:
		print("ERROR: INVALID TIME OBJECT REQUEST")
	timeObject.date = now
	timeObject.roomID = ID
	logList = importLog(ID, now, duration)
	timeObject.totalOccupants = getOccupants(logList, duration)
	timeObject.avgOccLength = calcAvgOccLength(logList, duration)
	timeObject.save()


def threadf(name):
	'''
	Seperate thread which creates time objects
	every hour/day/month/year. Everytime one of 
	those pass create an object with information
	from logs for each room 
	'''
	start = datetime.datetime.now()
	last = start

	floor3IDs = cache.get('floor3')
	floor4IDs = cache.get('floor4')
	now = datetime.datetime.now()
	while True:
		time.sleep(5)
		now = datetime.datetime.now()
		entered = False
		if now.day != last.day:
			for ID in floor3IDs:
				createTimeObject(ID,"day", last)
			for ID in floor4IDs:
				createTimeObject(ID,"day", last)
			entered = True
		if now.month != last.month:
			for ID in floor3IDs:
				createTimeObject(ID,"month", last)				
			for ID in floor4IDs:
				createTimeObject(ID,"month", last)
			entered = True
		if now.year != last.year:
			for ID in floor3IDs:
				createTimeObject(ID,"year", last)
			for ID in floor4IDs:
				createTimeObject(ID,"year", last)
			entered = True
		if entered:
			last = now


def startThread():
	print("Starting Thread")
	t = threading.Thread(target=threadf, args=(1,))
	t.setDaemon(True)
	t.start()

def importLog(ID, now, duration):	
	query = None
	if duration == 'day':
		query = StatsLog.objects.filter(roomID=ID, timeStamp__year=now.year, timeStamp__month=now.month, timeStamp__day=now.day)
	elif duration == 'month':
		query = Day.objects.filter(roomID=ID, timeStamp__year=now.year, timeStamp__month=now.month)
	elif duration == 'year':
		query = Month.objects.filter(roomID=ID, timeStamp__year=now.year)
	return query


def getOccupants(query, duration):
	'''
	Return the number of people in the room.
	Gets information from logs.
	'''
	if duration == 'day':
		return int(len(query)/2)
	elif duration == 'month':
		return query.aggregate(Sum(F('totalOccupants')))
	elif duration == 'year':
		return query.aggregate(Sum(F('totalOccupants')))
	return 0

def calcTimeDifference(query):
	timeDiff = []
	tmp_entry = None
	for log in query:
		# if the log contains entry data
		if log.event == 1:
			tmp_entry = log
		# else the log contains exit data
		else:
			timeDiff.append(log.timeStamp - tmp_entry.timeStamp)
	return timeDiff

def calcAvgOccLength(query, duration):
	'''
	Return the average amount of time
	the room has spent occupied. 
	Gets information from logs.
	'''
	if duration == 'day':
		timeDiff = calcTimeDifference(query)
		return sum(timeDiff, datetime.timedelta(0)) / len(timeDiff)
	elif duration == 'month':
		return query.aggregate(Avg(F('avgOccLength')))
	elif duration == 'year':
		return query.aggregate(Avg(F('avgOccLength')))
	return None