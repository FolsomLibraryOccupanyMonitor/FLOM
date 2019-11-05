from django.urls import path
from . import views

urlpatterns = [
	path('',views.index, name="index"),
]

print("Initializing stats...")
views.populateFloors()
