from django.shortcuts import render_to_response
from stats.models import Room
from stats.models import OccupancyStats
from stats.models import RoomUsage
from datetime import datetime



def index(request):
	'''
	@return display of stats page
	'''
	return render_to_response('stats/templates/html/stats.html')


def createObjects():
	roomTest = Room(roomID = "301", occupied = False,lastEntered = datetime.now(), lastExited = datetime.now(), roomType = "s" )
	occ = OccupancyStats(totalOccupancy = 5, averageDayOccupancy = 20, averageWeekOccupancy = 100, averageMonthOccupancy = 4000)
	roomTest.save()
	occ.save()