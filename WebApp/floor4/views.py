from django.shortcuts import render_to_response
from floor3.models import Room
from django.core.cache import cache
from django.template import RequestContext
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
	return cache.get("display4")


def createRooms():
	roomIDs = cache.get("floor4")
	x = 0
	for room in roomIDs:
		if(x%2 == 0):
			rooms[room] = Room(roomID = room, occupied = True)
		else:
			rooms[room] = Room(roomID = room, occupied = False)
		x = x + 1
	roomList = createDic()
	display = render_to_response('floor4/templates/html/floor4.html',roomList)
	cache.set("display4",display,None) 