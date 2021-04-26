from django import test
from django.test import Client
from django.test import TestCase
#import datetime
from .models import *
from .views import *
from datetime import date, datetime as dt
import pytz
from freezegun import freeze_time


"""
@call  'python3 manage.py test stats.simedgecases'

"""
class simulateEdgeCases(TestCase):
    #flush the databse
    c = Client()
    c.login(username='admin', password='admin')

    #day
    with freeze_time("2021-04-06 12:00:01"):
        c.get("http://127.0.0.1:8000/floor/enter/3/323C/pass")
    with freeze_time("2021-04-06 23:59:59"):
        time.sleep(8)
    with freeze_time("2021-04-07 12:00:01"):
        time.sleep(8)