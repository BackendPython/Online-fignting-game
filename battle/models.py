from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomeUser(AbstractUser):
    image = models.ImageField(default='static/images/user.png')


