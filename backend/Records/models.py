from django.db import models
from django.forms import ValidationError

class Tournament(models.Model):
    t_name = models.CharField(max_length=100)
    date = models.DateField()
    cardgame = models.CharField(max_length=200)
    
    def __str__(self):
        return self.t_name

class Player(models.Model):
    name = models.CharField(max_length=100)  
    phone = models.IntegerField()        
    totalwins = models.IntegerField()
    totalmatch = models.IntegerField()     

    def __str__(self):
        return self.name  # String representation of the model

class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE,related_name='matches')
    player1id = models.ForeignKey(Player, on_delete=models.CASCADE,related_name='matches1_id')
    player1 = models.CharField(max_length=100)
    player2id = models.ForeignKey(Player, on_delete=models.CASCADE,related_name='matches2_id')
    player2 = models.CharField(max_length=100)
    winner = models.CharField(max_length=100, blank=True, null=True)
    match_date = models.DateTimeField(auto_now_add=True)
    round = models.IntegerField()

    def __str__(self):
        return f"{self.player1} vs {self.player2} in {self.tournament}"

    def clean(self):
        if self.player1 == self.player2:
            raise ValidationError("Player1 and Player2 cannot be the same.")