from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render, redirect, reverse
from rest_framework.response import Response
from rest_framework import permissions
from battle.models import *
from battle.form import *
from battle.serializer import BattleApi

def home(request):
    return render(request, 'pages/home.html')

def signup(request):
    if request.method == 'POST':
        user_form = UserCreate(request.POST)
        if user_form.is_valid():
            user_form.save()
        return redirect('battle:home')
    else:
        user_form = UserCreate()
        
    context = {
        'user_form': user_form
    }
    
    return render(request, 'registration/signup.html', context)


def battle(request, pk):
    
    battle_id = Battle.objects.get(id=pk)
    
    context = {
        'battle_id': battle_id,
    }
    
    return render(request, 'pages/battle.html', context)

# ---------------------------------------------------------------- battle REST API ----------------------------------------------------------------

# get carusel
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def battle_api(request):
    battle = Battle.objects.all()
    serializer = BattleApi(battle, many=True)
    return Response(serializer.data)

# add battle
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def battle_add(request):
    serializer = BattleApi(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# search battle with id
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def battle_single(request, pk):
    battle = Battle.objects.get(id=pk)
    serializer = BattleApi(battle, many=False)
    return Response(serializer.data)

# edit battle
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def battle_single_edit(request, pk):
    battle = Battle.objects.get(id=pk)
    serializer = BattleApi(instance=battle, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# delete battle
@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))
def battle_single_delete(request, pk):
    krasovka = Battle.objects.get(id=pk)
    krasovka.delete()
    return Response("Successfull deleted")

# ---------------------------------------------------------------- battle REST API ----------------------------------------------------------------
