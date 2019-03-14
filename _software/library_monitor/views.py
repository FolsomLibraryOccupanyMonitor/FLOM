from django.http import HttpResponse
from django.core.cache import cache
from django.template import loader
import datetime
from _software.library_monitor.models import Log


# Create your views here.
def enter(request, room_id):
    cache.set(room_id, datetime.datetime.now(), None)
    return HttpResponse(f"You're entering room {room_id}.")


def leave(request, room_id):
    enter_time = cache.get(room_id)

    if enter_time is None:
        return HttpResponse('wut?')

    Log.objects.create(room_id=room_id, enter_time=enter_time,
                       leave_time=datetime.datetime.now())

    cache.set(room_id, None, None)
    Log.save()

    return HttpResponse(f"You're leaving room {room_id}.")


def check(request, floor_id):
    template = loader.get_template('library_monitor/index.html')
    rooms = cache.get('floor_' + str(floor_id))
    floor = cache.get_many(rooms)
    floor = {'floor': floor}
    return HttpResponse(template.render(floor, request))


def crypto_middleware(get_response):

    def middleware(request):
        # TODO: add some crypto stuff to the middleware

        response = get_response(request)

        return response

    return middleware
