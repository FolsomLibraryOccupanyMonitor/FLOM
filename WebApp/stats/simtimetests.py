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
    #this only works if run on an empty database
    #for some reason uses the production database
    #clear it to run with python3 manage.py flush

    '''
    I plan on adding asserts but struggling to 
    access the database through get_stats
    '''

    c = Client()
    c.login(username='admin', password='admin')

    #day
    with freeze_time("2021-04-06 12:00:01"):
        c.get("http://127.0.0.1:8000/floor/enter/3/323C/pass")
    with freeze_time("2021-04-06 12:30:01"):
        c.get("http://127.0.0.1:8000/floor/exit/3/323C/pass")
    with freeze_time("2021-04-07 12:00:01"):
        time.sleep(5)

    #month
    with freeze_time("2021-04-07 12:30:01"):
        c.get("http://127.0.0.1:8000/floor/enter/3/323C/pass")
    with freeze_time("2021-04-07 12:45:01"):
        c.get("http://127.0.0.1:8000/floor/exit/3/323C/pass")
    with freeze_time("2021-04-30 11:59:59"): #this would be the theoretical last date passed in april
        time.sleep(5)
    with freeze_time("2021-05-01 12:00:01"):
        time.sleep(5)

    #year
    with freeze_time("2021-05-06 12:00:01"):
        c.get("http://127.0.0.1:8000/floor/enter/3/323C/pass")
    with freeze_time("2021-05-06 12:30:01"):
        c.get("http://127.0.0.1:8000/floor/exit/3/323C/pass")
    with freeze_time("2021-05-07 12:30:01"):
        c.get("http://127.0.0.1:8000/floor/enter/3/323C/pass")
    with freeze_time("2021-05-07 12:45:01"):
        c.get("http://127.0.0.1:8000/floor/exit/3/323C/pass")
    with freeze_time("2021-12-31 11:59:59"): #this would be the theoretical last date passed in 2021
        time.sleep(5)
    with freeze_time("2022-01-01 12:00:01"):
        time.sleep(10)