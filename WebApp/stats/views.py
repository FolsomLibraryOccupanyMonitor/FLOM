from django.shortcuts import render_to_response
from stats.models import StatsLog
from floor.models import Room
from datetime import datetime
from django.core.cache import cache

def index(request):
	'''
	@return display of stats page
	'''
	return render_to_response('stats/templates/html/stats.html')

def log(rID, e):
	currLog = StatsLog(event = e, roomID = rID)
	currLog.save()
