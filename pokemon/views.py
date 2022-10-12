from webbrowser import get
from django.http import HttpResponse
from django.shortcuts import render
from .models import Pokemon
# Create your views here.


def get_home(request):
    return HttpResponse("HELLO")


def get_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)   # 1 = pokemon ID number
    return HttpResponse(pokemon)
