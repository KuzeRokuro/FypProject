from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json
import os
import pickle
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Records.models import Match, Tournament, Player
from Records.serializers import MatchSerializer

def fetchPlayers(request):
    players = Player.objects.all().values()  # Convert QuerySet to a list of dictionaries
    return JsonResponse(list(players), safe=False)  # Return as JSON

def fetchTournaments(request):
    tournaments = Tournament.objects.all().values()
    return JsonResponse(list(tournaments), safe=False)

def fetchMatches(request):
    match = Match.objects.all().values()
    return JsonResponse(list(match), safe=False)

class PlayerView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)  # Parse JSON payload
            name = data.get("name")
            phone = data.get("phone")
            totalwins = 0
            totalmatch = 0

            if not name or not phone:
                return JsonResponse({"error": "Missing required fields."}, status=400)

            # Create a new Player instance
            player = Player.objects.create(name=name, phone=phone, totalwins=0, totalmatch=0)

            return JsonResponse({"message": "Player created successfully!", "id": player.id}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
        
class TournamentView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)  # Parse JSON payload
            t_name= data.get("t_name")
            date= data.get("date")
            cardgame= data.get("cardgame")

            if not t_name or not date or not cardgame :
                return JsonResponse({"error": "Missing required fields."}, status=400)

            # Create a new Tournament instance
            tournament= Tournament.objects.create(t_name=t_name, date=date, cardgame=cardgame)

            return JsonResponse({"message": "Tournament created successfully!", "id": tournament.id}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
        
class MatchView(View):
    @api_view(['POST'])
    def match_list(request):
        if request.method == 'POST':
            data = request.data

            try:
                # Validate foreign key relationships
                tournament = Tournament.objects.get(id=data['tournament'])
                player1 = Player.objects.get(id=data['player1id'])
                player2 = Player.objects.get(id=data['player2id'])

                # Save the match
                match = Match.objects.create(
                    tournament=tournament,
                    player1id=player1,
                    player1=data.get('player1', player1.name),  # Use provided or default to DB name
                    player2id=player2,
                    player2=data.get('player2', player2.name),  # Use provided or default to DB name
                    winner=data.get('winner'),
                    round=data['round']
                )

                return Response(
                    {"message": "Match created successfully!", "id": match.id},
                    status=status.HTTP_201_CREATED,
                )

            except (Tournament.DoesNotExist, Player.DoesNotExist) as e:
                return Response(
                    {"error": str(e)},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            except KeyError as e:
                return Response(
                    {"error": f"Missing field: {e}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            except Exception as e:
                return Response(
                    {"error": str(e)},
                    status=status.HTTP_400_BAD_REQUEST,
                )

def players_by_tournament(request, tournament_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)
    matches = Match.objects.filter(tournament=tournament)
    player_names = set()
    for match in matches:
        player_names.add(match.player1)
        player_names.add(match.player2)
    players = Player.objects.filter(name__in=player_names)
    players_data = [{"id": player.id, "name": player.name} for player in players]
    return JsonResponse(players_data, safe=False)

import os
import pickle
from django.http import JsonResponse

from django.views import View
import json

# Define the path to the model file
model_path = os.path.join(os.path.dirname(__file__), 'Records', 'model.pkl')

# Load the model
with open(model_path, 'rb') as f:
    model = pickle.load(f)

@method_decorator(csrf_exempt, name='dispatch')
class PredictView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        # Process the input data and make predictions
        predictions = model.predict(data)
        return JsonResponse(predictions.tolist(), safe=False)

