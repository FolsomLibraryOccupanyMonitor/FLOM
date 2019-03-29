from django.http import HttpResponse
from django.core.cache import cache
from django.template import loader
# from django.http import Http404
from django.utils import timezone
from database.models import Log, Room
from django.core.exceptions import ObjectDoesNotExist
import datetime
# import pytz


# from django.db import models

# onetime load of rooms into db
def load_rooms(request):
    if cache.get('dev') == "True":
        floors = cache.get('floors')
        for floor_n in floors:
            rooms = cache.get('floor_' + floor_n)
            floor = cache.get_many(rooms)
            for room, stats in floor.items():
                room_d = Room(room_name=room, room_floor=floor_n)
                try:
                    room_db = Room.objects.get(room_name=room,
                                               room_floor=floor_n)
                except ObjectDoesNotExist:
                    room_d.save()
                except Exception as e:
                    print('ERROR Unexpected')
                    print(e)

    return check(request, '3')


def enter(request, room_id, secret_key):
    try:
        if secret_key not in cache.get("SECRET_KEYs"):
            return HttpResponse('You are not one of us!')
    except cache.get("SECRET_KEYs") is None:
        raise KeyError
    stats = cache.get(room_id)
    stats['occupied'] = True
    stats['e_time'] = timezone.now()
    cache.set(room_id, stats, None)
    return check(request, '3')


def leave(request, room_id, secret_key):
    try:
        if secret_key not in cache.get("SECRET_KEYs"):
            return HttpResponse('You are not one of us!')
    except cache.get("SECRET_KEYs") is None:
        raise KeyError
    stats = cache.get(room_id)
    if stats['e_time'] is None:
        return HttpResponse("Nobody is in the room!")

    try:
        room = Room.objects.get(room_name=room_id, room_floor=stats["floor"])

        log = Log(room_id=room, enter_time=stats["e_time"],
                  leave_time=timezone.now())
        log.save()

    except ObjectDoesNotExist:
        print('ERROR - RaspPi hit room that does not exist')
        return HttpResponse("ERROR - not real room")
    except Exception as e:
        print('ERROR Unexpected')
        print(e)
        return HttpResponse("ERROR - Unexpected")

    log_exists = True
    dao = 'None'
    dau = 'None'
    stats['occupied'] = False
    stats['last_enter'] = stats['e_time']
    stats['last_leave'] = timezone.now()
    stats['e_time'] = None
    try:
        total_logs = Log.objects.filter(room_id=room_db)
    except ObjectDoesNotExist:
        log_exists = False
    except Exception as e:
        print('ERROR Unexpected')
        print(e)
        log_exists = False

    if log_exists:
        dau_calc = 0
        day = []
        for log_items in total_logs:
            dau_calc += (
                        log_items.leave_time - log_items.enter_time).total_seconds()
            day.append(log_items.enter_time.timetuple().tm_yday)
        day = set(day)
        dau_calc /= len(total_logs)
        dau = str(datetime.timedelta(seconds=int(dau_calc)))
        dao = str(len(total_logs) // len(day))
    stats['dao'] = dao
    stats['dau'] = dau
    cache.set(room_id, stats, None)

    return check(request, '3')

def stats_page(request):
    template = loader.get_template('library_monitor/stats.html')
    available_stats = dict()
    available_stats['titles'] = ['Floor', 'Room #', 'Occupied', 'Last Entered',
                                 'Last Exited', 'Daily Average occupation',
                                 'Daily Average usage']
    available_stats['rooms'] = {}
    floors = cache.get('floors')
    for floor_n in floors:
        rooms = cache.get('floor_' + floor_n)
        floor = cache.get_many(rooms)
        for room, stats in floor.items():
            
            available_stats['rooms'][room] = stats.copy()
            occupancy = 'No'
            if stats["occupied"]:
                occupancy = 'Yes'
                available_stats['rooms'][room]['last_enter'] = stats['e_time']
                available_stats['rooms'][room]['last_leave'] = '---'
           
            available_stats['rooms'][room]['occupancy'] = occupancy
            available_stats['rooms'][room]['number'] = room
    available_stats = {'available_stats': available_stats}
    return HttpResponse(template.render(available_stats, request))


def check(request, floor_id):
    template = loader.get_template('library_monitor/floor' + floor_id + '.html')
    rooms = cache.get('floor_' + str(floor_id))
    floor = cache.get_many(rooms)
    floor = {'floor': floor}
    # print(floor)
    return HttpResponse(template.render(floor, request))


def about(request):
    template = loader.get_template('library_monitor/about.html')
    return HttpResponse(template.render({}, request))
