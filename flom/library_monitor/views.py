from django.http import HttpResponse
from django.core.cache import cache
import json


# Create your views here.
def enter(request, room_id):
    cache.set(room_id, True, None)
    return HttpResponse(f"You're entering room {room_id}.")


def leave(request, room_id):
    cache.set(room_id, False, None)
    return HttpResponse(f"You're leaving room {room_id}.")


def check(request, floor_id):
    rooms = cache.get('floor_' + str(floor_id))
    return cache.get_many(rooms)

