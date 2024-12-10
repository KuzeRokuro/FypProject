from django.http import JsonResponse
from .models import Tournament

def tournament_list(request):
    tournaments = list(Tournament.objects.values())
    return JsonResponse(tournaments, safe=False)
