from django.urls import path
from battle.views import *


app_name = 'battle'

urlpatterns = [
    path('', home, name='home'),
]