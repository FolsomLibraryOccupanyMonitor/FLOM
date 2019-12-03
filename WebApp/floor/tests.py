from django.test import TestCase
from . import views
from django.test import Client
from django.http import HttpResponse

# Create your tests here.
class BasicTestCase(TestCase):
    #Enter Room Success
    #Must Login to enter the room
    c = Client()
    c.login(username='admin', password='admin')
    #Enter Room
    response = c.get("http://127.0.0.1:8000/floor/enter/3/311/pass") #Response is of type byte
    response_string = (response.content).decode('ASCII') #To String
    assert(response_string == "Room successfully entered!")
    #Exit Room
    response = c.get("http://127.0.0.1:8000/floor/exit/3/311/pass") #Response is of type byte
    response_string = (response.content).decode('ASCII') #To String
    assert(response_string == "Room successfully exited!")

# Create your tests here.
class WrongRoom(TestCase):
    #Enter Room Success
    #Must Login to enter the room
    c = Client()
    c.login(username='admin', password='admin')
    #Enter Room
    response = c.get("http://127.0.0.1:8000/floor/enter/3/300/pass") #Response is of type byte
    response_string = (response.content).decode('ASCII') #To String
    assert(response_string == "Room Not Found")
    #Exit Room
    response = c.get("http://127.0.0.1:8000/floor/exit/3/300/pass") #Response is of type byte
    response_string = (response.content).decode('ASCII') #To String
    assert(response_string == "Room Not Found")
