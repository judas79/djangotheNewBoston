# from django.shortcuts import render
# Create your views here.

# added for lesson 13, 14 uncommented 15
# from django.template import loader

# added for lesson 15
from django.shortcuts import render

# added for lesson 16 to use 404 service
from django.http import Http404

# added in response to lesson 16 exception; using Album.Does.Not.Exist, NOT working
# use this with exception;  except ObjectDoesNotExist:
from django.core.exceptions import ObjectDoesNotExist

# commented out lesson 16; not used
# from django.http import HttpResponse

from . models import Album

# From lesson 13; commented out, not used
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

    return render(request, 'music/index.html', {'all_albums': all_albums})

    # lesson 13, 14 load our template contained in index.html, uncommented in lesson 15
    # template = loader.get_template('music/index.html')
    # this dictionary only consists of one pair in it.
    # commented out in lesson 16 and replaced, above
    '''
    context = {
        'all_albums': all_albums,
        }
    # render takes request as its first argument, then the filepath to that template
    return render(request, 'music/index.html', context)
    '''
    # for lesson 14 uncommented on lesson 15
    # return HttpResponse(template.render(context, request))



    # From an earlier lesson
    # return HttpResponse('<h1>response text goes in here</h1>')

# degressed
# def detail(request, album_id):
     # return HttpResponse('<h2>Details for Album ID:  ', str(album_id), '</h2>')

def detail(request, album_id):
    try:
        # get the id using the users passed in 'album_id'
        album = Album.objects.get(pk=album_id)
        # If the id is valid, this will work, if not an exception will be raised
    except ObjectDoesNotExist:  # using Album.Does.Not.Exist, from the lesson 16 does not work, use this with
                                # module:  from django.core.exceptions import ObjectDoesNotExist
        # to display the Http404 and a message 'whatever message you want to display'
        raise Http404('Album does not exist')
    # render takes request as its first argument, instead of passing in the dictionary 'context'
    # we pass in the album entry
    return render(request, 'music/detail.html', {'album': album})

    # commented out on lesson 16
    # return HttpResponse("<h2>Detail for Album ID: %s. " % album_id)

