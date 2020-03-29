from django.views import generic
# L30 to make a form to create an object
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album

#  L29 class with with template for the homepage
class IndexView(generic.ListView):
    template_name = 'music/index.html'

    # get all albums using get_queryset
    def get_queryset(self):
        return Album.objects.all()

# class with template for the details page
class DetailView(generic.DetailView):

    # get the model the user requested and template for the details page
    model = Album
    template_name = 'music/detail.html'

# class to add a new Album, we can inherit from CreateView
class AlbumCreate(CreateView):

# create the object; an Album:
    model = Album

# We will make fields as a list:
    fields = ['artist', 'album_title', 'genre', 'album_logo']

    # L31 comments area, to fix album_form.html template does not exist error
    template_name = 'music/album_form.html'
