from dataclasses import fields
from rest_framework import serializers
from battle.models import *

class BattleApi(serializers.ModelSerializer):
    class Meta:
        model = Battle
        fields = ['__all__']