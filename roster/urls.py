# app urls roster/urls.py
from django.conf.urls import patterns, url

from roster import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='roster_home'),
    url(r'^teams/$', views.teamsList, name='roster_teams_list'),
    url(r'^players/$', views.playersList, name='roster_players_list'),
    url(r'^teams/(?P<name>\w+)$', views.teams, name='roster_teams'),
    url(r'^players/(?P<pk>\d+)$', views.players, name='roster_players'),
    )
