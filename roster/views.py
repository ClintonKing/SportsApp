from django.shortcuts import render
from django.http import HttpResponse
from roster.models import Team, Player

# Create your views here.

def home(request):
    return render(request, "base.html")

def teams(request):
    teams = Team.objects.order_by('?')[0]
    return render(request, "roster/teams.html", {'teams': teams})

def players(request):
    players = Player.objects.order_by('?')[0]
    return render(request, "roster/players.html", {'players': players})
