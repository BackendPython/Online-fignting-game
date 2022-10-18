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




