from .models import Player,Tournament,Match
from rest_framework import serializers

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'name', 'phone','totalwins','totalmatch']


class TournamentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tournament
        fields = ['id','t_name','date','cardgame']

class MatchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Match
        fields = ['id', 'tournament','player1id','player1','player2id','player2','winner','match_date','round']