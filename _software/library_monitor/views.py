from django.http import HttpResponse
from django.core.cache import cache


# Create your views here.
def enter(request, room_id):
    cache.set(room_id, True, None)
    return HttpResponse(f"You're entering room {room_id}.")


def leave(request, room_id):
    cache.set(room_id, False, None)
    return HttpResponse(f"You're leaving room {room_id}.")


def check(request, room_id):
    return HttpResponse(f"room {room_id} is " +
                        'occupied' if cache.get(room_id) else 'unoccupied')
