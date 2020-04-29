from django.urls import path
from . import views

urlpatterns = [
	path('',views.index, name="index"), # This will find the corresponding view named "index"
]
