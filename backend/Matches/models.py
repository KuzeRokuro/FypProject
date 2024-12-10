from django.db import models
from Tournament.models import Tournament

class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE,related_name='matches')
    player1 = models.CharField(max_length=100)
    player2 = models.CharField(max_length=100)
    winner = models.CharField(max_length=100, blank=True, null=True)
    match_date = models.DateTimeField(auto_now_add=True)
    round = models.IntegerField()

    def __str__(self):
        return f"{self.player1} vs {self.player2}"