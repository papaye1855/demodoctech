from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def contact(request):
    return HttpResponse("Bienvenue sur la page contact")


def apropos(request):
    return HttpResponse("Ceci est la apge a-propos")