from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def signup(request):
    return render(request, 'registration/signup.html')
