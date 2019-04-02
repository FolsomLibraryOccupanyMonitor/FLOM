from django.urls import path, include
from . import views
from django.views.generic import RedirectView
from django.contrib import admin


urlpatterns = [
    # plain url boi
    # ex: /stats/
    path('stats/', views.stats_page, name='stats'),
    # ex: /about/
    path('about/', views.about, name='about'),
    # ex: /5/
    path('<str:floor_id>/', views.check, name='check'),
    # ex: /5/enter/
    path('<str:room_id>/enter/<secret_key>', views.enter, name='enter'),
    # ex: /5/leave/
    path('<str:room_id>/leave/<secret_key>', views.leave, name='leave'),
    # ex: /default path/
    path('',RedirectView.as_view(url='/accounts/login/'),name='login'),
    # ex: /admin
    path('admin/', admin.site.urls),
    # ex: /accounts
    path('accounts/',include('django.contrib.auth.urls')),
    # ex: /accounts/profile
    path('accounts/profile/', RedirectView.as_view(url='/3/'),name = 'check')


]