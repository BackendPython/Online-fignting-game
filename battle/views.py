from django.shortcuts import render, redirect, reverse
from battle.models import *
from battle.form import *

def home(request):
    return render(request, 'pages/home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('battle:home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html')
