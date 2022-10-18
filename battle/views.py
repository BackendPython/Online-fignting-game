from django.shortcuts import render, redirect, reverse
from battle.models import *
from battle.form import *

def home(request):
    return render(request, 'pages/home.html')

def signup(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('battle:home')
    else:
        user_form = UserCreationForm()
        
    context = {
        'user_form': user_form
    }
    
    return render(request, 'registration/signup.html', context)
