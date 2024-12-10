from django.contrib import admin
from .models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'totalwins','totalmatch')

class TournamentAdmin(admin.ModelAdmin):
    list_display = ()
