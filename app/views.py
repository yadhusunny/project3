from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def sunny(request):
    return HttpResponse('<h1><marquee>please check everything before you depart to trip</marquee></h1>')
def daisy(request):
    return HttpResponse('<h1><marquee>Daisy is my doggie</marquee></h1>')    