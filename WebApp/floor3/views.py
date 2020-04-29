from django.shortcuts import render_to_response
from django.http import HttpResponse
from floor3.models import Room
from django.core.cache import cache
from django.template import RequestContext
from datetime import datetime
# Create your views here. A view is a Python function that takes a web request and returns a web response.

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
	if ID in rooms.keys(): # If the Room is found in the "rooms" dictionary...
		currRoom = rooms[ID] # Store the value for the current room
		if currRoom.occupied: # If the current room is occupied...
			return HttpResponse("Room already occupied") # Respond that the room is already occupied
		else: # If the current room is NOT occupied
			currRoom.occupied = True # Set the current room to be occupied
			currRoom.lastEntered = datetime.now() # Keep track of when the room was entered
			currRoom.save() # Save the staus of the room to the database
			roomList = createDic() # See createDic() function above
			display = render_to_response('floor3/templates/html/floor3.html',roomList) # Update the floor3 template with updated rooms
			cache.set("display3",display,None) # Set new template as display3 variable
			return HttpResponse("Room successfully entered!") # Respond that the room has been successfully entered

	else: # If the Room is NOT found in the "rooms" dictionary...
		return HttpResponse("Room Not Found") # Respond that the room was not found

# ID = specific room's ID
def exitRoom(request,ID,password):
	if ID in rooms.keys(): # If the Room is found in the "rooms" dictionary...
		currRoom = rooms[ID] # Store the value for the current room
		if not currRoom.occupied: # If the current room is NOT occupied...
			return HttpResponse("Room already empty") # Respond that the room is already empty
		else: # If the current room is occupied...
			currRoom.occupied = False # Set the current room to be NOT occupied
			currRoom.lastExited = datetime.now() # Keep track of when the room was exited
			currRoom.save() # Save the status of the room to the database
			roomList = createDic() # See function createDic() above
			display = render_to_response('floor3/templates/html/floor3.html',roomList) # Update the floor3 template with updated rooms
			cache.set("display3",display,None) # Set new template as display3 variable
			return HttpResponse("Room successfully exited!") # Respond that the room has been successfully exited
	else: # If the room is NOT found in the "rooms" dictionary
		return HttpResponse("Room Not Found") # Respond that the room was not found



def createRooms(): # Fills the rooms dictionary
	roomIDs = cache.get("floor3") # Get all of the room IDs for rooms on floor3
	for room in roomIDs: # For every room on floor4...
		roomFound = Room.objects.filter(roomID = room).count() # Find if the room is found in the database (should equal 1)
		if roomFound > 0: # If the room was found...
			rooms[room] = Room.objects.get(roomID = room) # Put the room in the rooms dictionary
		else: # If the room was not found
			rooms[room] = Room(roomID = room, occupied = False, lastEntered = datetime.now(), lastExited = datetime.now()) # Create the room with initial states
			rooms[room].save() # Save the status of the room to the database

	roomList = createDic() # See function createDic() above
	display = render_to_response('floor3/templates/html/floor3.html',roomList) # Create new template with updated rooms
	cache.set("display3",display,None) # Set new template as display3 variable
