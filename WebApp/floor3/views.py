from django.shortcuts import render_to_response
from django.http import HttpResponse
from floor3.models import Room
from django.core.cache import cache
from django.template import RequestContext
from datetime import datetime
# Create your views here.

rooms = {} # Initially, rooms is an empty dictionary

# returns: a dictionary with ( key = "Rooms", value = list of rooms and their occupancy )
def createDic():
	roomList = {} # Initially, roomList is an empty dictionary
	roomList["Rooms"] = [] # Add an entry to the dictionary with ( key = "Rooms", value = empty list )
	for r in rooms: # For every room in the rooms dictionary...
		add = {"ID": rooms[r].roomID, "occupied" :rooms[r].occupied} 
		roomList["Rooms"].append(add) # Add the "add" value to the "Rooms" key in the roomList dictionary
	return roomList # Returns the filled roomList dictionary

# Returns the display for floor4
def index(request):
	return cache.get("display3")

# ID = the specific room's ID
def enterRoom(request,ID,password):
	if ID in rooms.keys():
		currRoom = rooms[ID]
		if currRoom.occupied:
			return HttpResponse("Room already occupied")
		else:
			currRoom.occupied = True
			currRoom.lastEntered = datetime.now()
			currRoom.save()
			roomList = createDic()
			display = render_to_response('floor3/templates/html/floor3.html',roomList)
			cache.set("display3",display,None)
			return HttpResponse("Room successfully entered!")

	else:
		return HttpResponse("Room Not Found")

def exitRoom(request,ID,password):
	if ID in rooms.keys():
		currRoom = rooms[ID]
		if not currRoom.occupied:
			return HttpResponse("Room already empty")
		else:
			currRoom.occupied = False
			currRoom.lastExited = datetime.now()
			currRoom.save()
			roomList = createDic()
			display = render_to_response('floor3/templates/html/floor3.html',roomList)
			cache.set("display3",display,None)
			return HttpResponse("Room successfully exited!")
	else:
		return HttpResponse("Room Not Found")



def createRooms():
	roomIDs = cache.get("floor3")
	for room in roomIDs:
		roomFound = Room.objects.filter(roomID = room).count()
		if roomFound > 0:
			rooms[room] = Room.objects.get(roomID = room)
		else:
			rooms[room] = Room(roomID = room, occupied = False, lastEntered = datetime.now(), lastExited = datetime.now())
			rooms[room].save()

	roomList = createDic()
	display = render_to_response('floor3/templates/html/floor3.html',roomList) # Create new template with updated rooms
	cache.set("display3",display,None) # Set new template as display3 variable
