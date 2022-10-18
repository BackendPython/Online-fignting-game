from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from battle.views import *


app_name = 'battle'

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('battle/', battle, name='battle'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]