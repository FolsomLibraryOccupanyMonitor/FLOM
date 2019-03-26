from django.http import HttpResponse
from django.core.cache import cache
from django.template import loader
from django.http import Http404
import datetime
from library_monitor.models import Log

def enter(request, room_id, secret_key):

    try:
        if secret_key not in cache.get("SECRET_KEYs"):
            return HttpResponse('You are not one of us!')
    except cache.get("SECRET_KEYs") is None:
        raise KeyError

    cache.set(room_id, datetime.datetime.now(), None)
    return check(request,'3')


def leave(request, room_id, secret_key):

    try:
        if secret_key not in cache.get("SECRET_KEYs"):
            return HttpResponse('You are not one of us!')
    except cache.get("SECRET_KEYs") is None:
        raise KeyError

    try:
        enter_time = cache.get(room_id)
    except enter_time is None:
        raise Http404("Nobody is in the room!")
    return check(request,'3')
  

def stats_page(request):
    template = loader.get_template('library_monitor/stats.html')
    available_stats = {}
    available_stats['titles'] = ['Floor','Room #', 'Occupied', 'Last Entered', \
                                 'Last Exited', 'Daily Average occupation', \
                                 'Daily Average usage']
    available_stats['rooms'] = {}
    floors = ['3','4']
    for floor_n in floors: 
        rooms = cache.get('floor_' + floor_n)
        floor = cache.get_many(rooms)
        for room, occupy in floor.items():
            occupancy = 'No'
            if occupy == True:
                occupancy = 'Yes'
            available_stats['rooms'][room] = {'floor' : floor_n, \
                                              'number' : room, \
                                              'occupied' : occupancy}
            available_stats['rooms'][room]['t_entered'] = 'NONE'
            available_stats['rooms'][room]['t_exited'] = 'NONE'
            available_stats['rooms'][room]['dao'] = 'NONE'
            available_stats['rooms'][room]['dau'] = 'NONE'
    available_stats = {'available_stats' : available_stats}
    return HttpResponse(template.render(available_stats, request))

    log = Log(room_id=room_id, enter_time=enter_time,
                       leave_time=datetime.datetime.now())

    log.save()
    cache.set(room_id, None, None)

    return HttpResponse(f"You're leaving room {room_id}.")


def check(request, floor_id):
    if floor_id == None:
        floor_id = '3'
    template = loader.get_template('library_monitor/floor'+\
                                   str(floor_id)+'.html')
    rooms = cache.get('floor_' + str(floor_id))
    floor = cache.get_many(rooms)
    floor = {'floor': floor}
    return HttpResponse(template.render(floor, request))

def about(request):
    template = loader.get_template('library_monitor/about.html')
    return HttpResponse(template.render({}, request))
