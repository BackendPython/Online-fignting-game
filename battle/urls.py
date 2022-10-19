from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from battle.views import *


app_name = 'battle'

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('battle/<int:pk>', battle, name='battle'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('battle', battle_api, name='battle'),
    path('battle-add', battle_add, name='battle_add'),
    path('battle-<int:pk>', battle_single, name='battle_single'),
    path('battle/edit/<int:pk>', edit_battle, name='edit_battle'),
    path('battle-edit/<int:pk>', battle_single_edit, name='battle_single_edit'),
    path('battle-delete/<int:pk>', battle_single_delete, name='battle_single_delete'),
]