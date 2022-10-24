from rest_framework import serializers
from battle.models import *

class BattleApi(serializers.ModelSerializer):
    class Meta:
        model = Battle
        fields = '__all__'
        
class Battle2_Api(serializers.ModelSerializer):
    class Meta:
        model = Battle_tic_tacoe
        fields = '__all__'