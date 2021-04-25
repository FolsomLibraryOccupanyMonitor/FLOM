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

    pass