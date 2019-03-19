from django.http import HttpResponse
from django.core.cache import cache
from django.template import loader
from django.shortcuts import render
import json


def flr3(request):
    return render(request, 'library_monitor/floor3.html')

def stats_page(request):
    template = loader.get_template('library_monitor/stats.html')
    available_stats = {}
    available_stats['titles'] = ['Floor','Room #', 'Occupied', 'Last Entered', 'Last Exited', 'Daily Average occupation', 'Daily Average usage']
    available_stats['rooms'] = {}
    floors = ['3','4']
    for floor_n in floors: 
        rooms = cache.get('floor_' + floor_n)
        floor = cache.get_many(rooms)
        for room, occupy in floor.items():
            occupancy = 'No'
            if occupy == True:
                occupancy = 'Yes'
            available_stats['rooms'][room] = {'floor' : floor_n, 'number' : room, 'occupied' : occupancy}
            available_stats['rooms'][room]['t_entered'] = 'NONE'
            available_stats['rooms'][room]['t_exited'] = 'NONE'
            available_stats['rooms'][room]['dao'] = 'NONE'
            available_stats['rooms'][room]['dau'] = 'NONE'
    available_stats = {'available_stats' : available_stats}
    return HttpResponse(template.render(available_stats, request))


def enter(request, room_id):
    cache.set(room_id, True, None)
    return HttpResponse(f"You're entering room {room_id}.")


def leave(request, room_id):
    cache.set(room_id, False, None)
    return HttpResponse(f"You're leaving room {room_id}.")


def check(request, floor_id):
    template = loader.get_template('library_monitor/floor'+str(floor_id)+'.html')
    rooms = cache.get('floor_' + str(floor_id))
    floor = cache.get_many(rooms)
    floor = {'floor': floor}
    return HttpResponse(template.render(floor, request))
