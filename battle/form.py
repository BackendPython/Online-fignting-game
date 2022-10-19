from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from battle.models import *
from django import forms

User = get_user_model()

class UptadeUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email',]
        
        
class UserCreate(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", 'email', 'age', 'region', 'bio')
        field_classes = {"username":UsernameField}
        
class EditBattle(forms.ModelForm):
    class Meta:
        model = Battle
        fields = '__all__'