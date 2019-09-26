from django.urls import path
from . import views


'''
index - This will find the corresponding view named "index"
enterRoom - This will find the corresponding view named enterRoom
exitRoom - This will find the correspoding view named "exitRoom"
'''
urlpatterns = [
	path('',views.index, name="index"),
	path("enter/<ID>/<password>",views.enterRoom, name = "enterRoom"),
	path("exit/<ID>/<password>", views.exitRoom, name= "exitRoom")
]
