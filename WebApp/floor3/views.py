from django.shortcuts import render_to_response
from django.http import HttpResponse
from floor3.models import Room
from django.core.cache import cache
from django.template import RequestContext
from datetime import datetime
# Create your views here.

rooms = {}
def createDic():
	roomList = {}
	roomList["Rooms"] = []
	for r in rooms:
		add = {"ID": rooms[r].roomID, "occupied" :rooms[r].occupied}
		roomList["Rooms"].append(add)
	return roomList

def index(request):
	return cache.get("display3")

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
	display = render_to_response('floor3/templates/html/floor3.html',roomList)
	cache.set("display3",display,None)
