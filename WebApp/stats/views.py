from django.shortcuts import render_to_response
from stats.models import OccupancyStats, RoomUsage
from floor.models import Room
from datetime import datetime
from django.core.cache import cache

roomUsages = {}

def index(request):
	'''
	@return display of stats page
	'''
	return render_to_response('stats/templates/html/stats.html')

def getUpdatedRoomUsagesList():
	roomUsagesList = {}
	roomUsagesList['RoomUsages'] = []
	for ID, roomUsage in roomUsages.items():
		add = {'Room #':ID, 
			   'Last Entered':roomUsage.room.lastEntered,
			   'Last Exited':roomUsage.room.lastExited,
			   'Currently Occupied':roomUsage.room.occupied,
			   'Room Type':roomUsage.room.roomType,
			   'Total Visitors':roomUsage.occupancyStats.totalOccupancy,
			   'Average Day Occupancy':roomUsage.occupancyStats.averageDayOccupancy,
			   'Average Week Occupancy':roomUsage.occupancyStats.averageDayOccupancy,
			   'Average Month Occupancy':roomUsage.occupancyStats.averageMonthOccupancy,
			   'Longest Time in Room':roomUsage.largestHoursInRoom }
		roomUsagesList['RoomUsages'].append(add)
	return roomUsagesList

def createRooms(IDs):
	'''
	Iterates through list of possible IDs and checks database for existence.
	If the object exists, it gets it from the database and places it in the roomUsages dictionary.
	Otherwise, it creates a new RoomUsage object and places it in the roomUsages dictionary.
	@modifies roomUsages
	'''
	# iterate through each ID
	for ID in IDs:
		# check if room is in the database (1 = found, 0 = not found)
		roomFound = Room.objects.filter(roomID = ID).count()
		if roomFound > 0:
			# get Room from database and look for corresponding RoomUsage object
			room = Room.objects.get(roomID=ID)
			roomUsageFound = RoomUsage.objects.filter(room=room).count()
			if roomUsageFound > 0:
				# put existing RoomUsage object in roomUsages
				roomUsages[ID] = RoomUsage.objects.get(room=room)
			else:
				# create new roomUsage with current room and initialize occupancy stats
				occupancy = OccupancyStats()
				occupancy.save()
				roomUsages[ID] = RoomUsage(room=room, occupancyStats=occupancy, currentDate=datetime.now()) 
		else:
			# create new room with ID, not occupied, and current datetimes
			room = Room(roomID = ID, occupied = False, lastEntered = datetime.now(), lastExited = datetime.now())
			occupancy = OccupancyStats()
			room.save()
			occupancy.save()
			roomUsages[ID] = RoomUsage(room=room, occupancyStats=occupancy, currentDate=datetime.now())
		# save the status of the room to the database
		roomUsages[ID].save()

def populateFloors():
	'''
	Fills the roomUsages dictionary with key = {ID}, value = {RoomUsage} (see RoomUsage object definition in models.py)
	Function call found in ./urls.py
	@modifies roomUsages
	'''
	# get the room IDs from the cache for the floor
	floor3IDs = cache.get('floor3')
	floor4IDs = cache.get('floor4')
	# create rooms for each floor
	createRooms(floor3IDs)
	createRooms(floor4IDs)
	# create an updated list of rooms to render to the webpage 
	roomUsagesList = getUpdatedRoomUsagesList()
	display = render_to_response('stats/templates/html/stats.html',roomUsagesList)
	cache.set("displayStats",display,None)

