from django.db import models

class Tournament(models.Model):
    t_name = models.CharField(max_length=100)
    date = models.DateField()
    cardgame = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
