from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)  
    phone = models.IntegerField()             

    def __str__(self):
        return self.field1  # String representation of the model