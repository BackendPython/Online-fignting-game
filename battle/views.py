from django.shortcuts import render, redirect, reverse
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
    
    battle = Battle.objects.all()
    battle_empty = Battle.objects.filter(all_players=2)
    battle_id = Battle.objects.filter(id=pk)
    
    context = {
        'battle_all': battle,
        'battle_id': battle_id,
        'battle_empty': battle_empty,
    }
    
    return render(request, 'pages/battle.html', context)
