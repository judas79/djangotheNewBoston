# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>response text goes in here</h1>')

#def detail(request, album_id):
    #return HttpResponse('<h2>Details for Album ID:  ', str(album_id), '</h2>')


def detail(request, album_id):
    return HttpResponse("<h2>Detail for Album ID: %s. " % album_id)

