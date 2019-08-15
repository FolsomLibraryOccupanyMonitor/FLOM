from django.shortcuts import render_to_response
from django.http import HttpResponse
from floor3.models import Room
from django.core.cache import cache
from django.template import RequestContext
# Create your views here. A view is a Python function that takes a web request and returns a web response.

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
	if ID in rooms.keys(): # If the Room is found in the "rooms" dictionary...
		currRoom = rooms[ID] # Store the value for the current room
		if currRoom.occupied: # If the current room is occupied...
			return HttpResponse("Room already occupied") # Respond that the room is already occupied
		else: # If the current room is NOT occupied...
			currRoom.occupied = True # Set the current room to be occupied
			roomList = createDic() 
			display = render_to_response('floor4/templates/html/floor4.html',roomList) # Update the floor4 image on the website
			cache.set("display4",display,None) # Display the image of floor4 with filled rooms
			return HttpResponse("Room successfully entered!") # Respond that the room has been successfully occupied

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
			roomList = createDic()
			display = render_to_response('floor4/templates/html/floor4.html',roomList) # Update the floor4 image on the website
			cache.set("display4",display,None) # Display the image of floor4 with filled rooms
			return HttpResponse("Room successfully exited!") # Respond that the room has been successfully exited

def createRooms(): # Fills the rooms dictionary
	roomIDs = cache.get("floor4") # Get all of the roomIDs for rooms on floor 4
	for room in roomIDs: # For every room on floor4...
		rooms[room] = Room(roomID = room, occupied = False) # Add an entry in the rooms dictionary, where each new room is intially NOT occupied
	roomList = createDic()
	display = render_to_response('floor4/templates/html/floor4.html',roomList) # Update the floor4 image on the website
	cache.set("display4",display,None) # Display the image of floor 4
