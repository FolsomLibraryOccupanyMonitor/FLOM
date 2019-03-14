from django.urls import path
from . import views

urlpatterns = [
    # plain url boi
    path('', views.flr3, name='flr3'),
    # ex: /library_monitor/5/
    path('<int:floor_id>/', views.check, name='check'),
    # ex: /library_monitor/5/enter/
    path('<int:room_id>/enter/', views.enter, name='enter'),
    # ex: /library_monitor/5/leave/
    path('<int:room_id>/leave/', views.leave, name='leave'),
]