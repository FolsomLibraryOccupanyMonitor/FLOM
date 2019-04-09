from django.http import HttpResponse
from django.core.cache import cache
from django.template import loader, TemplateDoesNotExist
# from django.http import Http404
from django.utils import timezone
from database.models import Log, Room, Occupy
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseNotFound, Http404
import datetime
import time


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

# onetime load of enter and leave to db
def enter_leave_allrooms(request):
    if cache.get('dev') == "True":
        floors = cache.get('floors')
        for floor_n in floors:
            rooms = cache.get('floor_' + floor_n)
            floor = cache.get_many(rooms)
            for room, stats in floor.items():
                print(room)
                print(cache.get("SECRET_KEYs")[room])
                enter(request, room, cache.get("SECRET_KEYs")[room])
                time.sleep(10)
                leave(request, room, cache.get("SECRET_KEYs")[room])

    return check(request, '3')


def enter(request, room_id, secret_key):
    try:
        if secret_key != cache.get("SECRET_KEYs")[room_id]:
            if cache.get('dev_login') == "True":
                if secret_key != 'aaaaaa':
                    raise Http404("Dev: Invalid Address")
            else:
                raise Http404("Invalid Address")
    except Exception as e:
        print(e)
        raise Http404()
    stats = cache.get(room_id)
    time = datetime.datetime.now()
    if stats['occupied']:
        raise Http404('Room already occupied')
    try:
        room = Room.objects.get(room_name=room_id, room_floor=stats["floor"])
        ocppy = None
        try:
            ocppy = Occupy.objects.get(room_id=room)
            ocppy.time = time
        except ObjectDoesNotExist:
            ocppy = Occupy(room_id=room, time=time)
        ocppy.save()
    except ObjectDoesNotExist:
        print('ERROR - RaspPi hit room that does not exist')
        raise Http404()
    except Exception as e:
        print('ERROR Unexpected')
        # print(e)
        raise Http404()

    stats['occupied'] = True
    stats['e_time'] = time
    cache.set(room_id, stats, None)

    return HttpResponse('entered room')


def leave(request, room_id, secret_key):
    print(request)
    try:
        if secret_key != cache.get("SECRET_KEYs")[room_id]:
            if cache.get('dev') == "True":
                if secret_key != 'aaaaaa':
                    raise Http404("Dev: Invalid Address")
            else:
                raise Http404("Invalid Address")
    except Exception as e:
        print(e)
        raise Http404()

    stats = cache.get(room_id)
    if stats['e_time'] is None:
        raise Http404('Room wasn\'t occupied')
    time = timezone.make_aware(datetime.datetime.now(),
                               timezone.get_current_timezone())
    try:
        room = Room.objects.get(room_name=room_id, room_floor=stats["floor"])

        log = Log(room_id=room, enter_time=stats["e_time"],
                  leave_time=time)
        log.save()
    except ObjectDoesNotExist:
        print('ERROR - RaspPi hit room that does not exist')
        raise Http404()
    except Exception as e:
        print('ERROR Unexpected')
        # print(e)
        raise Http404()

    log_exists = True
    dao = 'None'
    dau = 'None'
    stats['occupied'] = False
    t = timezone.make_aware(stats['e_time'],
                            timezone.get_current_timezone())
    stats['last_enter'] = t.strftime('%Y-%m-%d %I:%M %p')
    stats['last_leave'] = time.strftime('%Y-%m-%d %I:%M %p')
    stats['e_time'] = None
    try:
        total_logs = Log.objects.filter(room_id=room)
    except ObjectDoesNotExist:
        log_exists = False
    except Exception as e:
        print('ERROR Unexpected')
        # print(e)
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

    return HttpResponse('left room')


def stats_page(request):
    try:
        template = loader.get_template('library_monitor/stats.html')
        available_stats = dict()
        available_stats['titles'] = ['Floor', 'Room #', 'Occupied',
                                     'Last Entered', 'Last Exited',
                                     'Daily Average occupation',
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
                    t = stats['e_time'].astimezone(
                        timezone.get_current_timezone())
                    available_stats['rooms'][room]['last_enter'] = \
                        t.strftime('%Y-%m-%d %I:%M %p')
                    available_stats['rooms'][room]['last_leave'] = '---'
                # recent_log.enter_time.strftime('%c')
                available_stats['rooms'][room]['occupancy'] = occupancy
                available_stats['rooms'][room]['number'] = room
        available_stats = {'available_stats': available_stats}
        return HttpResponse(template.render(available_stats, request))

    except TemplateDoesNotExist:
        raise Http404()
    except Exception as e:
        print(e)
        raise Http404("Unexpected ERROR")


def check(request, floor_id):
    try:

        template = loader.get_template(
            'library_monitor/floor' + floor_id + '.html')
        rooms = cache.get('floor_' + str(floor_id))
        floor = cache.get_many(rooms)
        floor = {'floor': floor}
        return HttpResponse(template.render(floor, request))
    except TemplateDoesNotExist:
        raise Http404()
    except Exception as e:
        print(e)
        raise Http404("Unexpected ERROR")


def about(request):
    try:

        template = loader.get_template('library_monitor/about.html')
        return HttpResponse(template.render({}, request))
    except TemplateDoesNotExist:
        raise Http404()
    except:
        raise Http404("Unexpected ERROR")

