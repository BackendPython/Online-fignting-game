from django.urls import path

app_name = 'battle'

urlpatterns = [
    path('', home, name='home'),
]