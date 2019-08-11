from django.urls import path
from . import views

urlpatterns = [
	path('',views.index, name="index"),
	path("enter/<ID>/<password>",views.enterRoom, name = "enterRoom"),
	path("exit/<ID>/<password>", views.exitRoom, name= "exitRoom")
]
