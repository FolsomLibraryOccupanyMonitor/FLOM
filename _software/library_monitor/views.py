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

"""
Database setup functions:

    load_rooms()
    enter_leave_allrooms()

    These functions are used, for only once in the begining, to set up 
    room data and occupancy data.
"""

#load_rooms() gets each room number and floor number from cache
#   and puts the room information into Room database table.
def load_rooms(request):
    if cache.get('dev') == "True":
        floors = cache.get('floors')
        for floor_number in floors:
            rooms = cache.get('floor_' + floor_number)
            floor = cache.get_many(rooms)
            for room, stats in floor.items():
                room_d = Room(room_name=room, room_floor=floor_number)

                #Try to find a specific room in DB
                #If object is not found, save the new room instace into DB
                try:
                    room_db = Room.objects.get(room_name=room,
                                               room_floor=floor_number)
                except ObjectDoesNotExist:
                    room_d.save()
                except Exception as e:
                    print('ERROR Unexpected')
                    print(e)

    return check(request, '3')

#enter_leave_allrooms() creates arbitrary enter and leave log
#   and puts them into Occupancy database table.
def enter_leave_allrooms(request):
    if cache.get('dev') == "True":
        floors = cache.get('floors')
        for floor_number in floors:
            rooms = cache.get('floor_' + floor_number)
            floor = cache.get_many(rooms)
            for room, stats in floor.items():
                enter(request, room, cache.get("SECRET_KEYs")[room])
                time.sleep(10)
                leave(request, room, cache.get("SECRET_KEYs")[room])

    return check(request, '3')


"""
URL patterns

    enter()
    leave()
    stats_page()
    check()
    about()

    These functions handle the HTTP calls.
"""


#enter() handles all of the processes that should be 
#	handled once a person enters a room.
def enter(request, room_id, secret_key):
	#if secret_key is not valid, we don't process the fucntion
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

    room_stat = cache.get(room_id)
    current_time = datetime.datetime.now()

    if stats['occupied']:
        raise Http404('Room already occupied')

    try:
        room = Room.objects.get(room_name=room_id, room_floor=stats["floor"])
        ocppy = None

        #Uppdate occupy information for specific room in DB
        try:
            ocppy = Occupy.objects.get(room_id=room)
            ocppy.time = current_time
        except ObjectDoesNotExist:
            ocppy = Occupy(room_id=room, time=current_time)
        ocppy.save()
    except ObjectDoesNotExist:
        print('ERROR - RaspPi hit room that does not exist')
        raise Http404()
    except Exception as e:
        print('ERROR Unexpected')
        raise Http404()

    #Update room stat in cache
    room_stat['occupied'] = True
    room_stat['e_time'] = current_time
    cache.set(room_id, room_stat, None)
    return HttpResponse('entered room')

#leave() handles all of the processes that should be 
#	handled once a person leaves a room.
def leave(request, room_id, secret_key):
	#if secret_key is not valid, we don't process the fucntion
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

    room_stat = cache.get(room_id)
    if room_stat['e_time'] is None:
        raise Http404('Room wasn\'t occupied')
    current_time = timezone.make_aware(datetime.datetime.now(),
                               timezone.get_current_timezone())
    try:
        room = Room.objects.get(room_name=room_id, room_floor=room_stat["floor"])

        #Once someoen leaves a room log is updated
        log = Log(room_id=room, enter_time=room_stat["e_time"],
                  leave_time=current_time)
        log.save()
    except ObjectDoesNotExist:
        print('ERROR - RaspPi hit room that does not exist')
        raise Http404()
    except Exception as e:
        print('ERROR Unexpected')
        raise Http404()

    log_exists = True
    dao = 'None'
    dau = 'None'
    room_stat['occupied'] = False
    last_enter_time = timezone.make_aware(room_stat['e_time'],
                            timezone.get_current_timezone())

    #Update last_enter, last_leave, and enter time accordingly
    room_stat['last_enter'] = last_enter_time.strftime('%Y-%m-%d %I:%M %p')
    room_stat['last_leave'] = current_time.strftime('%Y-%m-%d %I:%M %p')
    room_stat['e_time'] = None
    try:
        total_logs = Log.objects.filter(room_id=room)
    except ObjectDoesNotExist:
        log_exists = False
    except Exception as e:
        print('ERROR Unexpected')
        log_exists = False

    #If log of the room exists, calculate the average occupancy time
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

#stats_page() creates the template for stats page.
#	It displays latest status and statistics for each room.
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
                available_stats['rooms'][room]['occupancy'] = occupancy
                available_stats['rooms'][room]['number'] = room
        available_stats = {'available_stats': available_stats}
        return HttpResponse(template.render(available_stats, request))

    except TemplateDoesNotExist:
        raise Http404()
    except Exception as e:
        print(e)
        raise Http404("Unexpected ERROR")

#check() creates the template for live occupancy display of given floor.
#	It displays image of given floor and occupancy of each room in it.
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

#about() creates the template for about page.
#	It displays information about the project.
def about(request):
    try:

        template = loader.get_template('library_monitor/about.html')
        return HttpResponse(template.render({}, request))
    except TemplateDoesNotExist:
        raise Http404()
    except:
        raise Http404("Unexpected ERROR")


