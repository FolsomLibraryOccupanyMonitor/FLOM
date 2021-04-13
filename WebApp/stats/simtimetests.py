from django import test
from django.test import Client
from django.test import TestCase
#import datetime
from .models import *
from .views import *
from datetime import date, datetime as dt
import pytz
from freezegun import freeze_time


class simulateTime(TestCase):
    c = Client()
    c.login(username='admin', password='admin')
    with freeze_time("2021-04-06 12:00:01"):
        c.get("http://127.0.0.1:8000/floor/enter/3/323C/pass")
    with freeze_time("2021-04-06 12:30:01"):
        c.get("http://127.0.0.1:8000/floor/exit/3/323C/pass")
    with freeze_time("2021-04-07 12:00:01"):
        time.sleep(10)


# class simulateTime(TestCase):
# 	c = Client()
# 	c.login(username='admin', password='admin')
# 	with freeze_time("2021-01-01 12:00:01"):
# 		#Enter Room
# 		c.get("http://127.0.0.1:8000/floor/enter/3/311/pass")
# 	with freeze_time("2021-01-01 12:30:01"):
# 		c.get("http://127.0.0.1:8000/floor/exit/3/311/pass")
# 	with freeze_time("2021-01-02 12:00:01"):
# 		time.sleep(10)
# 		stats = get_stats(311)
#         print(stats['day'])