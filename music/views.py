# from django.shortcuts import render
# Create your views here.

#added for lesson 13
from django.template import loader
from django.http import HttpResponse
from . models import Album

# From lesson 13
'''
def index(request):
    # use Album.objects.all() to get all albums
    all_albums = Album.objects.all()
    # make html a string
    html = ''
    # iterate through all albums
    for album in all_albums:
        # get urls
        url = '/music/' + str(album.id) + '/'
        # convert url to html for a website link
        html += '<a href="' + url + '">' + album.album_title + '</a><br>'
    return HttpResponse(html)
'''

def index(request):

    # use Album.objects.all() to get all albums
    all_albums = Album.objects.all()
    # load our template contained in index.html
    template = loader.get_template('music/index.html')
    context = {
        'all_albums': all_albums,
        }
    return HttpResponse(template.render(context, request))



    #From an earlier lesson
    #return HttpResponse('<h1>response text goes in here</h1>')

# degressed
# def detail(request, album_id):
     #return HttpResponse('<h2>Details for Album ID:  ', str(album_id), '</h2>')

def detail(request, album_id):
    return HttpResponse("<h2>Detail for Album ID: %s. " % album_id)

