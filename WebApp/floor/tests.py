from django.test import TestCase
from . import views
from django.test import Client
from django.http import HttpResponse

# Create your tests here.
class BasicTestCase(TestCase):
    #Testing a get request
    c = Client()
    c.login(username='admin', password='admin')
    response = c.get("http://127.0.0.1:8000/floor/enter/3/311/pass")
    response_string = (response.content).decode('ASCII')
    print("Get:", response_string)
