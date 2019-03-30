from django.http import HttpResponse
from django.core.cache import cache
from django.template import loader
from django.http import Http404
from django.utils import timezone
from database.models import Log, Room
from django.core.exceptions import ObjectDoesNotExist
import datetime
import pytz
# from django.db import models

# onetime load of rooms into db
def load_rooms(request):
    if cache.get('dev') == "True":
        floors = ['3','4']
        for floor_n in floors: 
            rooms = cache.get('floor_' + floor_n)
            floor = cache.get_many(rooms)
            for room, tup in floor.items():
                room_d = Room(room_name=room,room_floor=floor_n)
                try:
                    room_db = Room.objects.get(room_name=room,room_floor=floor_n)
                except ObjectDoesNotExist:
                    room_d.save()
                except Exception as e: 
                    print('ERROR Unexpected')
                    print(e)
                    
    return check(request,'3')



def enter(request, room_id, secret_key):

    try:
        if room_id not in cache.get("SECRET_KEYs"):
            return HttpResponse(cache.get(room_id))
            return HttpResponse('You are not one of us!')
    except cache.get("SECRET_KEYs") is None:
        raise KeyError
    cache.set(room_id, (True, timezone.now()), None)
    return check(request,'3')


def leave(request, room_id, secret_key):
    try:
        room_id = str(room_id)
        if secret_key not in cache.get(room_id):
            return HttpResponse('You are not one of us!')
    except cache.get(room_id) is None:
        raise KeyError
    occupy, enter_time = cache.get("SECRET_KEYs")
    if enter_time is None:
        return HttpResponse("Nobody is in the room!")

    # try:

    room = Room.objects.get(room_name=room_id,room_floor=room_id[0])

    log = Log(room_id=room, enter_time=enter_time,
                       leave_time=timezone.now())
    log.save()
    cache.set(room_id, (False,None), None)

    # except:

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
        for room, tup in floor.items():
            occupy, e_time = tup
            occupancy = 'No'
            if occupy != False:
                occupancy = 'Yes'
            log_exists = True
            room_db = None
            recent_log = None
            t_entered = 'None'
            t_exited = 'None'
            total_logs = None
            available_stats['rooms'][room] = {'floor' : floor_n, 'number' : room, 'occupied' : occupancy}
            dao = 'None'
            dau = 'None'
            try:
                room_db = Room.objects.get(room_name=room,room_floor=floor_n)
                recent_log= Log.objects.filter(room_id=room_db).latest('id')
                total_logs = Log.objects.filter(room_id=room_db)
            except ObjectDoesNotExist:
                log_exists = False
            except Exception as e: 
                print('ERROR Unexpected')
                print(e)
                log_exists = False
            if occupy != False: 
                t_entered = e_time.strftime('%c')
                t_exited = '---'
            elif log_exists:
                t_entered = recent_log.enter_time.strftime('%c')
                t_exited = recent_log.leave_time.strftime('%c')

            available_stats['rooms'][room]['t_entered'] = t_entered
            available_stats['rooms'][room]['t_exited'] = t_exited

            if log_exists:
                dao_calc = 0
                dau_calc = 0
                day = []
                for log_items in total_logs:
                    dau_calc += (log_items.leave_time-log_items.enter_time).total_seconds()
                    day.append(log_items.enter_time.timetuple().tm_yday)
                day = set(day)
                dau_calc/=len(total_logs)
                dau = str(datetime.timedelta(seconds=dau_calc))
                dao = str(len(total_logs)//len(day))

            available_stats['rooms'][room]['dao'] = dao
            available_stats['rooms'][room]['dau'] = dau

    available_stats = {'available_stats' : available_stats}
    return HttpResponse(template.render(available_stats, request))

def check(request, floor_id):
    template = loader.get_template('library_monitor/floor'+floor_id+'.html')
    rooms = cache.get('floor_' + str(floor_id))
    floor = cache.get_many(rooms)
    floor = {'floor': floor}
    print(floor)
    return HttpResponse(template.render(floor, request))

def about(request):
    template = loader.get_template('library_monitor/about.html')
    return HttpResponse(template.render({}, request))
