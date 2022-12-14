from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render, redirect, reverse
from rest_framework.response import Response
from battle.serializer import Battle2_Api, BattleApi
from rest_framework import permissions
from django.http import HttpResponse, JsonResponse
from battle.models import *
from battle.form import *

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

def battle2(request, pk):
    
    battle_single = Battle_tic_tacoe.objects.get(id=pk)
    
    context = {
        'battle_single': battle_single,
    }
    
    return render(request, 'pages/tictacoe.html', context)
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

# ---------------------------------------------------------------- battle REST API ----------------------------------------------------------------

# get api
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def battle2_api(request):
    battle = Battle_tic_tacoe.objects.all()
    serializer = Battle2_Api(battle, many=True)
    return Response(serializer.data)

# add battle
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def battle2_add(request):
    serializer = Battle2_Api(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# search battle with id
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def battle2_single(request, pk):
    battle = Battle_tic_tacoe.objects.get(id=pk)
    serializer = Battle2_Api(battle, many=False)
    return Response(serializer.data)

# edit battle
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def battle2_single_edit(request, pk):
    battle = Battle_tic_tacoe.objects.get(id=pk)
    serializer = Battle2_Api(instance=battle, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# delete battle
@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))
def battle2_single_delete(request, pk):
    krasovka = Battle_tic_tacoe.objects.get(id=pk)
    krasovka.delete()
    return Response("Successfull deleted")

# ---------------------------------------------------------------- battle REST API ----------------------------------------------------------------




def battle_create(request):
    battle_edit = Battle.objects.count()
    if request.method == 'POST':
        rate_form = EditBattle(request.POST)
        if rate_form.is_valid():
            rate_form.save()
    else:
        rate_form = EditBattle()
    return render(request, 'pages/battle-create.html', {})
        

# def all_players_count(request):
# 	if request.method == "POST":
# 		el_id = request.POST.get("el_id")
# 		val = request.POST.get("all_players")
# 		rate = Battle.objects.get(id=el_id)
# 		rate.all_players = val
# 		rate.save()
# 		return JsonResponse({"success": "true", "score": val})
# 	return JsonResponse({"success": "false"})
