from django.http.response import HttpResponse
from django.shortcuts import render

from etudiants.models import Etudiants

def index(request):
    etudiants = Etudiants.objects.all()
    return render(request,"index.html",{"etudiants":etudiants})

def contact(request):
    return HttpResponse("Bienvenue sur la page contact")


def apropos(request):
    return HttpResponse("Ceci est la apge a-propos")