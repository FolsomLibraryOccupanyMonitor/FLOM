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
	pass
	# start = datetime.datetime.now()
	# lastHour = start.hour
	# lastDay = start.day
	# lastMonth = start.month
	# lastYear = start.year

	# floor3IDs = cache.get('floor3')
	# floor4IDs = cache.get('floor4')
	# while(True):
	# 	time.sleep(5)
	# 	now = datetime.datetime.now()
	# 	if (now.hour != lastHour):
	# 		lastHour = now.hour
	# 		for ID in floor3IDS:
	# 			TimeFrame hr = new TimeFrame()
	# 			hr.date = now 
	# 			hr.roomPointer = Room.objects.get(roomID=ID)
	# 			hr.span = "hour"
	# 			hr.roomID = ID
	# 			#placeholder syntax
	# 			log = importLog(ID, now)
	# 			hr.totalOccupants = log.occupants
	# 			hr.avgOccLength = log.occupantLength
	# 			hr.save()
	# 		for ID in floor4IDs:
	# 			TimeFrame hr = new TimeFrame()
	# 			hr.date = now
	# 			hr.roomPointer = Room.objects.get(roomID=ID)
	# 			hr.span = "hour"
	# 			#placeholder syntax
	# 			log = importLog(ID, now)
	# 			hr.totalOccupants = log.occupants
	# 			hr.avgOccLength = log.occupantLength
	# 			hr.save()
	# 		print("An hour has passed")
	# 	if (now.day != lastDay):
	# 		lastDay = now.day
	# 		print("A day has passed")
	# 	if (now.month != lastMonth):
	# 		lastMonth = now.month
	# 		print("A month has passed")
	# 	if (now.year != lastYear):
	# 		lastYear = now.year
	# 		print("A year has passed")
		
def startThread():
	t = threading.Thread(target=threadf, args=(1,))
	t.setDaemon(True)
	t.start()

def importLog(ID, now):
	pass