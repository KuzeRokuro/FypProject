from django.http import JsonResponse
from .models import Match

def match_list(request):
    matches = list(Match.objects.values())
    return JsonResponse(matches, safe=False)
