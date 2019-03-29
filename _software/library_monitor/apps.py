import sys
from django.apps import AppConfig


class LibraryMonitorConfig(AppConfig):
    name = 'library_monitor'

    def ready(self):
        if 'runserver' not in sys.argv:
            return True
        # you must import your modules here 
        # to avoid AppRegistryNotReady exception

        from database.models import Log, Room
        from django.core.exceptions import ObjectDoesNotExist
        from django.core.cache import cache
        from django.utils import timezone
        import datetime

        # startup code here - LOADING CACHE

        for floor in cache.get('floors'):
            rooms = cache.get('floor_' +floor)
            for room_id in rooms:
                stats = cache.get(room_id)
                log_exists = True
                try:
                    room_db = Room.objects.get(room_name=room_id, room_floor=floor)
                    recent_log = Log.objects.filter(room_id=room_db).latest('id')
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
                    stats['dau'] = str(datetime.timedelta(seconds=int(dau_calc)))
                    stats['dao'] = str(len(total_logs) // len(day))
                    stats['last_enter'] = recent_log.enter_time.strftime('%c')
                    stats['last_leave'] = recent_log.leave_time.strftime('%c')

                cache.set(room_id, stats, None)


