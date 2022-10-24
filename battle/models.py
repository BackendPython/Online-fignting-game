from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomeUser(AbstractUser):
    image = models.ImageField()
    age = models.IntegerField(default=20)
    victory = models.IntegerField(default=0)
    defeats = models.IntegerField(default=0)
    all_fighting = models.IntegerField(default=0)
    region = models.CharField(default="Uzbekistan", max_length=50)
    bio = models.CharField(default="I'm best fighter in the world", max_length=200)


class Battle(models.Model):
    all_players = models.IntegerField(default=0)
    first_player = models.CharField(max_length=50)
    second_player = models.CharField(max_length=50)
    player_heal = models.IntegerField(default=100)
    player_left = models.IntegerField(default=2)
    player_attack = models.IntegerField(default=10)
    player_jump = models.BooleanField(default=False)
    player_winner = models.BooleanField(default=False)
    player_blow_turn = models.BooleanField(default=False)
    rival_heal = models.IntegerField(default=100)
    rival_attack = models.IntegerField(default=10)
    riavl_right = models.IntegerField(default=2)
    rival_jump = models.BooleanField(default=False)
    rival_winner = models.BooleanField(default=False)
    rival_blow_turn = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.first_player} vs {self.second_player}"
    
class Battle_tic_tacoe(models.Model):
    first_player = models.CharField(max_length=50)
    second_player = models.CharField(max_length=50)
    rival_turn = models.BooleanField(default=False)
    player_turn = models.BooleanField(default=False)
    rival_winner = models.BooleanField(default=False)
    player_winner = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.first_player} vs {self.second_player}"

