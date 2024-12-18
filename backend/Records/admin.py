from django.contrib import admin
from .models import Player,Tournament,Match

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'totalwins','totalmatch')

@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ('t_name','date','cardgame')

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('tournament','player1id','player1','player2id','player2','winner','match_date','round')
