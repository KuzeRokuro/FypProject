from django.http import JsonResponse
from django.shortcuts import render
from .models import Player  # Import your Player model

# View to fetch all players and return them as JSON
def get_players(request):
    players = Player.objects.all()  # Fetch all players
    players_list = list(players.values())  # Convert QuerySet to a list of dictionaries
    return JsonResponse(players_list, safe=False)

# View to display players on a webpage (optional)
def players_page(request):
    players = Player.objects.all()
    return render(request, 'players.html', {'players': players})

def homepage(request):
    return render(request, 'homepage.html')