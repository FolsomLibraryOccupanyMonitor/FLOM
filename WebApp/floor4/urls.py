from django.urls import path
from . import views

urlpatterns = [ 
	path('',views.index, name="index"), # This will find the corresponding view named "index"
	path("enter/<ID>/<password>",views.enterRoom, name = "enterRoom"), # This will find the corresponding view named "enterRoom" 
	path("exit/<ID>/<password>", views.exitRoom, name= "exitRoom") # This will find the corresponding view named "exitRoom"
]

print('Creating rooms for floor4...')
views.createRooms()
