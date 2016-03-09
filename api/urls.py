
from django.conf.urls import url, include
from django.contrib import admin

from api import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?i)route/(?P<origin>[a-zA-Z0-9._-]+)/(?P<destination>[a-zA-Z0-9._-]+)/$', views.get_route_name),
    url(r'^(?i)route/(?P<origin>[0-9]+)/(?P<destination>[0-9]+)/$', views.get_route_id),
    url(r'^(?i)distance/(?P<origin>[a-zA-Z0-9._-]+)/(?P<destination>[a-zA-Z0-9._-]+)/$', views.get_distance_name),
    url(r'^(?i)distance/(?P<origin>[0-9]+)/(?P<destination>[0-9]+)/$', views.get_distance_id),
    url(r'^(?i)data/(?P<solarSystemID>[0-9]+)/(?P<victimShipID>[0-9]+)/(?P<x>[0-9]+)/(?P<y>[0-9]+)/(?P<z>[0-9]+)/$', views.get_data),

]
