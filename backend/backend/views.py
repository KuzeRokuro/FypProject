from django.http import JsonResponse
from Records.models import Player, Tournament, Match

def fetchPlayers(request):
    players = Player.objects.all().values()  # Convert QuerySet to a list of dictionaries
    return JsonResponse(list(players), safe=False)  # Return as JSON

def fetchTournaments(request):
    tournaments = Tournament.objects.all().values()
    return JsonResponse(list(tournaments), safe=False)

def fetchMatches(request):
    match = Match.objects.all().values()
    return JsonResponse(list(match), safe=False)