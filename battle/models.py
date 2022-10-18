from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomeUser(AbstractUser):
    pass

class UserProfile(models.Model):
    img = models.ImageField(default='static/images/user.png')
