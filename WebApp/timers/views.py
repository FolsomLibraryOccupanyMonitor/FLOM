from django.shortcuts import render
import threading
import time
import datetime

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