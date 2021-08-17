from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count 

from . import team_maker

def index(request):
  
  context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
    "baseball": League.objects.filter(sport__contains="baseball"),
    "women": League.objects.filter(name__contains="women"),
    "hockey": League.objects.filter(sport__contains="hockey"),
    "notfootball": League.objects.exclude(sport__contains="football"),
    "conference": League.objects.filter(name__contains="conference"),
    "atlantic": League.objects.filter(name__contains="Atlantic"),
    "dallasteams": Team.objects.filter(location="Dallas"),
    "raptors": Team.objects.filter(team_name__contains='Raptors'),
    "city": Team.objects.filter(location__contains='City'),
    "tfirst": Team.objects.filter(team_name__startswith='T'),
    "orderbylocation": Team.objects.all().order_by('location'),
    "orderbyname": Team.objects.all().order_by('-team_name'),
    "playercooper": Player.objects.filter(last_name='Cooper'),
    "playerjoshua": Player.objects.filter(first_name='Joshua'),
    "cooperbutnotjoshua": Player.objects.filter(last_name='Cooper').exclude(first_name='Joshua'),
    "alexanderorwyatt": Player.objects.filter(first_name ='Alexander')|Player.objects.filter(first_name='Wyatt'),
	}

  return render(request, "leagues/index.html", context)

def index2(request):

  context = {

		"leagues": League.objects.all(),

		"teams": Team.objects.all(),

		"players": Player.objects.all(),

    "atlanticcityconf": Team.objects.filter(league__name = "Atlantic Soccer Conference"),

    "bospenplayers": Player.objects.filter(curr_team__location="Boston", curr_team__team_name="Penguins"),

    "intcolbasecon": Player.objects.filter(curr_team__league__name="International Collegiate Baseball Conference"),

    "lopezfootballplayer": Player.objects.filter(curr_team__league__name="American Conference of Amateur Football").filter(last_name="Lopez"),

    "footballplayers": Player.objects.filter(curr_team__league__sport="Football"),

    "sophiaplayer": Team.objects.filter(all_players__first_name="Sophia"),

    "sophialeagueplayer": League.objects.filter(teams__all_players__first_name="Sophia"),

    "floresnot": Player.objects.filter(last_name='Flores').exclude(curr_team__team_name='Roughriders', curr_team__location='Washington'),

    "samuelevansteams": Team.objects.filter(curr_players__first_name='Samuel', curr_players__last_name='Evans', all_players__first_name='Samuel', all_players__last_name='Evans'),

    "tigercats": Player.objects.filter(curr_team__team_name='Tiger-Cats', curr_team__location='Manitoba', all_teams__team_name='Tiger-Cats', all_teams__location='Manitoba'),

    "formerwichitavikings": Player.objects.filter(all_teams__team_name='Vikings', all_teams__location='Wichita').exclude(curr_team__team_name='Vikings', curr_team__location='Wichita'),

    "formerteamsjacobgray": Team.objects.filter(all_players__first_name='Jacob', all_players__last_name = 'Gray'). exclude(team_name='Colts', location = 'Oregon'),

    "joshuabaseleague": Player.objects.filter(first_name='Joshua', all_teams__league__name='Atlantic Federation of Amateur Baseball Players'),

    "twelveplayers": Team.objects.annotate(Count('curr_players')).annotate(Count('all_players')).filter(curr_players__count__gte=12).filter(all_players__count__gte=12),

    "allplayers": Player.objects.all().annotate(Count('all_teams')).order_by('all_teams__count'),
	}

  return render(request, "leagues/index2.html", context)

def make_data(request):
  team_maker.gen_leagues(10)
  team_maker.gen_teams(50)
  team_maker.gen_players(200)

  return redirect("index")