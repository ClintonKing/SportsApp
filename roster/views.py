from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from roster.models import Team, Player

# Create your views here.

def home(request):
    context = {
        'player_count': Player.objects.count(),
        'team_count': Team.objects.count(),
    }
    return render(request, "roster/home.html", context)

def teams(request, name):
    teams = get_object_or_404(Team, name=name)
    return render(request, "roster/teams.html", {'team': teams})

def players(request, pk):
    players = get_object_or_404(Player, id=pk)
    return render(request, "roster/players.html", {'player': players})

def teamsList(request):
    teams_list = Team.objects.all().order_by('pk')
    return render(request, 'roster/teams_list.html', {'teams': teams_list})

def playersList(request):
    players_list = Player.objects.all()
    return render(request, 'roster/players_list.html', {'players': players_list})
