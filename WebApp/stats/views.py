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
	available_stats = {}
	available_stats['titles'] = ['Date', 'Total Occupants', 'Average Occupancy Time']
	available_stats['row_info'] = {'id':[], 'date':[], 'total_occupants':[], 'occupancy_time':[]}
	query = None
	if duration == 'day':
		query = Day.objects.all();
	elif duration == 'month':
		query = Month.objects.all();
	else:
		query = Year.objects.all();
	available_stats['range'] = range(len(query))
	for obj in query:
		available_stats['row_info']['id'].append(obj.roomID)
		available_stats['row_info']['date'].append(obj.date)
		available_stats['row_info']['total_occupants'].append(obj.totalOccupants)
		available_stats['row_info']['occupancy_time'].append(obj.avgOccLength)
	display = render_to_response('stats/templates/html/stats.html', available_stats)
	cache.set('basic_stats_display', display)
	return HttpResponse('Statistics displayed for ' + duration)

@login_required
def index(request):
	'''
	@return display of stats page
	'''
	return cache.get('basic_stats_display')

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
	lastHour = start.hour
	lastDay = start.day
	lastMonth = start.month
	lastYear = start.year

	floor3IDs = cache.get('floor3')
	floor4IDs = cache.get('floor4')
	now = datetime.datetime.now()
	while True:
		time.sleep(5)
		now = datetime.datetime.now()
		if now.day != lastDay:
			lastDay = now.day
			for ID in floor3IDs:
				createTimeObject(ID,"day",now)
			for ID in floor4IDs:
				createTimeObject(ID,"day",now)
		if now.month != lastMonth:
			lastMonth = now.month
			for ID in floor3IDs:
				createTimeObject(ID,"month",now)				
			for ID in floor4IDs:
				createTimeObject(ID,"month",now)
		if now.year != lastYear:
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