from django.http import HttpResponse
from django.core.cache import cache
from django.template import loader
from django.http import Http404
import datetime
from library_monitor.models import Log


def flr3(request):
    return render(request, 'library_monitor/floor3.html')


def enter(request, room_id, secret_key):

    if secret_key != 'ok':
        return HttpResponse('You are not one of us!')

    cache.set(room_id, datetime.datetime.now(), None)
    return HttpResponse(f"You're entering room {room_id}.")


def leave(request, room_id, secret_key):

    if secret_key != 'ok':
        return HttpResponse('You are not one of us!')

    try:
        enter_time = cache.get(room_id)
    except enter_time is None:
        raise Http404("Nobody is in the room!")

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
