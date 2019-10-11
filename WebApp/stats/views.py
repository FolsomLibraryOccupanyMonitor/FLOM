from django.shortcuts import render_to_response
from stats.models import statsLog
from floor.models import Room
from datetime import datetime
from django.core.cache import cache

roomUsages = {}

def index(request):
	'''
	@return display of stats page
	'''
	return render_to_response('stats/templates/html/stats.html')

def log(rp, rID, e):
	currLog = statsLog(roomPointer = rp, event = e,roomID = rID)
	currLog.save()
