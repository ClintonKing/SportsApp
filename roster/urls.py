# app urls roster/urls.py
from django.conf.urls import patterns, url

from roster import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='roster_home'),
    url(r'^teams/$', views.teams, name='roster_teams'),
    url(r'^players/$', views.players, name='roster_players'),
    )
