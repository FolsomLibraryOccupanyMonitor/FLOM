<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
	path('',views.index, name="index"),
]

views.startThread()
=======
from django.urls import path
from . import views

urlpatterns = [
	path('',views.index, name="index"),
]

print("Initializing stats...")
views.populateFloors()
>>>>>>> e9737a5266941e0a426839fa6578143eced7d5a2
