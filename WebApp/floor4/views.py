from django.shortcuts import render_to_response
from django.http import HttpResponse
from floor4.models import Room
from django.core.cache import cache
from django.template import RequestContext
from datetime import datetime
# Create your views here.

rooms = {} # Initially, rooms is an empty dictionary

# returns: a dicationary with ( key = "Rooms", value = list of rooms and their occupancy )
def createDic(): 
	roomList = {} # Initially, roomList is an empty dictionary
	roomList["Rooms"] = [] # Add an entry to the dictionary with ( key = "Rooms", value = empty list )
	for r in rooms: # For every room in the rooms dictionary...
		add = {"ID": rooms[r].roomID, "occupied" :rooms[r].occupied} 
		roomList["Rooms"].append(add) # Add the "add" value to the "Rooms" key in the roomList dictionary
	return roomList # Returns the filled roomList dictionary

# Returns the display for floor4
def index(request):
	return cache.get("display4")

# ID = the specific room's ID
def enterRoom(request,ID,password):
	if ID in rooms.keys():	# If the Room is found in the "rooms" dictionary...
		currRoom = rooms[ID]	# If the current room is occupied...
		if currRoom.occupied:	
			return HttpResponse("Room already occupied")	# Respond that the room is already occupied
		else:	# If the current room is NOT occupied...
			currRoom.occupied = True	# Set the current room to be occupied
			currRoom.lastEntered = datetime.now() # Saving last entered
			currRoom.save()	# saving to database
			roomList = createDic()	# See createDic() function above
			display = render_to_response('floor4/templates/html/floor4.html',roomList)# Update floor4 template with updated rooms
			cache.set("display4",display,None)	# Set new template as display4 variable
			return HttpResponse("Room successfully entered!")
	else: # If the Room is NOT found in the "rooms" dictionary...
		return HttpResponse("Room Not Found") # Respond that the room was not found

# ID = specific room's ID
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
			display = render_to_response('floor4/templates/html/floor4.html',roomList)
			cache.set("display4",display,None)
			return HttpResponse("Room successfully exited!")

def createRooms():
	roomIDs = cache.get("floor4")
	for room in roomIDs:
		roomFound = Room.objects.filter(roomID = room).count()
		if roomFound > 0:
			rooms[room] = Room.objects.get(roomID = room)
		else:
			rooms[room] = Room(roomID = room, occupied = False, lastEntered = datetime.now(), lastExited = datetime.now())
			rooms[room].save()
	roomList = createDic()
	display = render_to_response('floor4/templates/html/floor4.html',roomList)
	cache.set("display4",display,None)
