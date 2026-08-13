from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def inicio(resquest):
    return HttpResponse("<H1>Pico pal que lee</H1>")