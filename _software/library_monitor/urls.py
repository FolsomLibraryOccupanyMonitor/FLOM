from django.urls import path
from . import views
from django.views.generic import RedirectView


urlpatterns = [
    # plain url boi
    # ex: /default path/
    path('',RedirectView.as_view(url='/3/'),name='check'),
    # ex: /5/
    path('<int:floor_id>/', views.check, name='check'),
    # ex: /5/enter/
    path('<int:room_id>/enter/<secret_key>', views.enter, name='enter'),
    # ex: /5/leave/
    path('<int:room_id>/leave/<secret_key>', views.leave, name='leave'),
    # ex: /stats/
    path('stats/', views.stats_page, name='stats'),
    # ex: /about/
    path('about/', views.about, name='about'),


]