from django.http import HttpResponse
from django.core.cache import cache
from django.template import loader
from django.shortcuts import render
import json


def flr3(request):
    return render(request, 'library_monitor/floor3.html')


def enter(request, room_id):
    cache.set(room_id, True, None)
    return HttpResponse(f"You're entering room {room_id}.")


def leave(request, room_id):
    cache.set(room_id, False, None)
    return HttpResponse(f"You're leaving room {room_id}.")


def check(request, floor_id):
    template = loader.get_template('library_monitor/index.html')
    rooms = cache.get('floor_' + str(floor_id))
    floor = cache.get_many(rooms)
    floor = {'floor': floor}
    return HttpResponse(template.render(floor, request))
