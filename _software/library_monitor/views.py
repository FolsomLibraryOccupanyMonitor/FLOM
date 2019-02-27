from django.http import HttpResponse
from django.core.cache import cache

from django.shortcuts import render
import json


# Create your views here.
def enter(request, room_id):
    cache.set(room_id, True, None)
    return HttpResponse(f"You're entering room {room_id}.")


def leave(request, room_id):
    cache.set(room_id, False, None)
    return HttpResponse(f"You're leaving room {room_id}.")


def check(request, floor_id):
    template_name = 'library_monitor/index.html'
    rooms = cache.get('floor_' + str(floor_id))
    floor = cache.get_many(rooms)
    return render(request, 'library_monitor/index.html', floor)
