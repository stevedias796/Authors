from django.contrib import admin
from django.urls import path
from .views import * #impoprting all functions from views

urlpatterns = [
    path('', home),
    path('home/',home),
    path('home_new/',new_home),
    path('search/',searching),
    
]
