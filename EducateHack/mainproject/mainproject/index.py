from django.http import HttpResponse
from django.shortcuts import render
from core.views import index, updateindex


def index(request):
    return render(request, "index.html")


def updateindex(request):
    results = respond.Get['Major']
    return render(request, "updateindex.html", {'Major': results})
