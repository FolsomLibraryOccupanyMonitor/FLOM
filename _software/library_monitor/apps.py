import sys
from django.apps import AppConfig
import pytz

local_tz = pytz.timezone('America/New_York')


def utc_to_local(utc_dt):
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_tz.normalize(local_dt)


class LibraryMonitorConfig(AppConfig):
    name = 'library_monitor'

    def ready(self):
        # if 'runserver' not in sys.argv:
        #     return True
        # you must import your modules here 
        # to avoid AppRegistryNotReady exception

        from database.models import Log, Room, Occupy
        from django.core.exceptions import ObjectDoesNotExist
        from django.core.cache import cache
        from django.utils import timezone
        import datetime, os

        # startup code here - LOADING CACHE
        # if os.environ.get('RUN_MAIN', None) != 'true':
        print("starting startup")
        for floor in cache.get('floors'):
            rooms = cache.get('floor_' + floor)
            for room_id in rooms:
                stats = cache.get(room_id)
                log_exists = True
                room_db = None
                ocppy_log = None
                ocuppied_currently = True
                try:
                    room_db = Room.objects.get(room_name=room_id,
                                               room_floor=floor)
                    recent_log = Log.objects.filter(room_id=room_db).latest(
                        'id')
                    total_logs = Log.objects.filter(room_id=room_db)
                except ObjectDoesNotExist:
                    log_exists = False
                except Exception as e:
                    print('ERROR Unexpected')
                    print(e)
                    log_exists = False
                try:
                    ocppy_log = Occupy.objects.get(room_id=room_db)
                except ObjectDoesNotExist:
                    ocuppied_currently = False
                except Exception as e:
                    print('ERROR Unexpected')
                    print(e)
                    ocuppied_currently = False
                if log_exists:
                    dau_calc = 0
                    day = []
                    for log_items in total_logs:
                        dau_calc += (log_items.leave_time -
                                     log_items.enter_time).total_seconds()
                        day.append(log_items.enter_time.timetuple().tm_yday)
                    day = set(day)
                    dau_calc /= len(total_logs)
                    stats['dau'] = str(
                        datetime.timedelta(seconds=int(dau_calc)))
                    stats['dao'] = str(len(total_logs) // len(day))
                    stats['last_enter'] = utc_to_local(
                        recent_log.enter_time).strftime(
                        '%Y-%m-%d %I:%M %p')
                    stats['last_leave'] = utc_to_local(
                        recent_log.leave_time).strftime(
                        '%Y-%m-%d %I:%M %p')
                    if ocuppied_currently:
                        if recent_log.leave_time < ocppy_log.time:
                            stats['last_enter'] = ocppy_log.time.strftime(
                                '%Y-%m-%d %I:%M %p')
                            stats['last_leave'] = '---'
                            stats['e_time'] = ocppy_log.time
                            stats['occupied'] = True
                elif ocuppied_currently:
                    stats['last_enter'] = \
                        ocppy_log.time.strftime('%Y-%m-%d %I:%M %p')
                    stats['last_leave'] = '---'
                    stats['e_time'] = ocppy_log.time
                    stats['occupied'] = True

                cache.set(room_id, stats, None)
        cache.set('initialized', True, None)
        # print(cache.get('initialized'))
        print("ended startup")
