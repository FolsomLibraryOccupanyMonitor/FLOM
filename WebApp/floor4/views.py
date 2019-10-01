from django.shortcuts import render_to_response
from django.http import HttpResponse
from floor4.models import Room
from django.core.cache import cache
from django.template import RequestContext
from datetime import datetime
# Create your views here. A view is a Python function that takes a web request and returns a web response.

rooms = {} # Initially, rooms is an empty dictionary

def getUpdatedRoomsList():
	'''
	Creates an updated version of the rooms list used for updating the webpage
	@return a dictionary with (key = "Rooms", value = list of rooms and their occupancy)
	'''
	# create an empty dictionary and add key "Rooms" with empty list as value
	roomList = {}
	roomList["Rooms"] = []
	# iterate through all the rooms on the floor
	# 	get room data to add
	# 	append room data to roomList
	for r in rooms:
		add = {"ID": rooms[r].roomID, "occupied" :rooms[r].occupied} 
		roomList["Rooms"].append(add)
	return roomList

def index(request):
	'''
	@return the display for floor4
	'''
	return cache.get("display4")

def enterRoom(request,ID,password):
	'''
	This function is called when someone enters a room
	@modifies Room object with matching ID
	@return Response to server
	'''
	# Check for room existence
	if ID in rooms.keys():
		currRoom = rooms[ID]
		# if the current room is already occupied
		if currRoom.occupied:
			return HttpResponse("Room already occupied")
		else:
			# modify current room to occupied = True and update current datetime
			currRoom.occupied = True
			currRoom.lastEntered = datetime.now()
			# save changes made to current room (to database)
			currRoom.save()
			# create the dictionary of rooms needed to update webpage
			roomList = getUpdatedRoomsList()
			# set the cache with the new room display based on changes made
			display = render_to_response('floor4/templates/html/floor4.html',roomList)
			cache.set("display4",display,None)
			return HttpResponse("Room successfully entered!")
	# Room not found
	else:
		return HttpResponse("Room Not Found")

def exitRoom(request,ID,password):
	'''
	This function is called when someone exits a room
	@modifies Room object with matching ID
	@return Response to server
	'''
	# Check for room existence
	if ID in rooms.keys():
		currRoom = rooms[ID]
		# if the room is empty
		if not currRoom.occupied:
			return HttpResponse("Room already empty")
		else:
			# modify current room to occupied = False and update current datetime
			currRoom.occupied = False
			currRoom.lastExited = datetime.now()
			# save changes made to current room (to database)
			currRoom.save()
			# create dictionary of rooms needed to update webpage
			roomList = getUpdatedRoomsList()
			# set the cache with the new room display based on changes made
			display = render_to_response('floor4/templates/html/floor4.html', roomList)
			cache.set("display4",display,None)
			return HttpResponse("Room successfully exited!")
	# Room not found
	else:
		return HttpResponse("Room Not Found")


def createRooms():
	'''
	Fills the rooms dictionary with key = {ID}, value = {Room} (see Room object definition in models.py)
	Should only be called once at startup
	@modifies rooms
	'''
	# get the room IDs from the cache for the floor
	roomIDs = cache.get("floor4")
	# iterate through each ID
	for ID in roomIDs:
		# check if room is in the database (1 = found, 0 = not found)
		roomFound = Room.objects.filter(roomID = ID).count()
		if roomFound > 0:
			# put existing room in rooms dict
			rooms[ID] = Room.objects.get(roomID = ID)
		else:
			# create new room with ID, not occupied, and current datetimes
			rooms[ID] = Room(roomID = ID, occupied = False, lastEntered = datetime.now(), lastExited = datetime.now()) 
			# save the status of the room to the database
			rooms[ID].save()

	# create an updated list of rooms to render to the webpage 
	roomList = getUpdatedRoomsList()
	display = render_to_response('floor4/templates/html/floor4.html',roomList)
	cache.set("display4",display,None)
