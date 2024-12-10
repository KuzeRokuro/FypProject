from django.http import JsonResponse
from django.shortcuts import render
from .models import Player,Tournament,Match
from rest_framework import permissions, viewsets
from .serializers import PlayerSerializer, TournamentSerializer, MatchSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Player.objects.all().order_by('id')
    serializer_class = PlayerSerializer
    # permission_classes = [permissions.IsAuthenticated]


class TournamentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Tournament.objects.all().order_by('id')
    serializer_class = TournamentSerializer
    # permission_classes = [permissions.IsAuthenticated]

class MatchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Match.objects.all().order_by('id')
    serializer_class = MatchSerializer
    # permission_classes = [permissions.IsAuthenticated]