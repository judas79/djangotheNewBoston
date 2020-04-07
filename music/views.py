from django.views import generic
# L30 to make a form to create an object
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# L32  from django.core.urlresolvers import reverse_lazy (DEPRECIATED v2)
from django.urls import reverse_lazy
from .models import Album

# L34 redirect to a specified page,
# authenticate check that the username password is in the data base,
# login assigns session ID for authorization to all website pages, without logging in to each
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View


# L34 import local . class form.py class UserForm
from .forms import UserForm

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

# L30 class to add a new Album, we can inherit from CreateView
class AlbumCreate(CreateView):

    # create the object; an Album:
    model = Album

# We will make fields as a list:
    fields = ['artist', 'album_title', 'genre', 'album_logo']

    # L31 comments area, to fix album_form.html template does not exist error
    template_name = 'music/album_form.html'

# L32 class to edit(update) an Album, we can inherit from UpdateView
class AlbumUpdate(UpdateView):

    # create the object; an Album:
    model = Album

# We will make fields as a list:
    fields = ['artist', 'album_title', 'genre', 'album_logo']

# L32 class to delete an Album, we can inherit from DeleteView
class AlbumDelete(DeleteView):

    # create the object; an Album:
    model = Album

    # redirect user to home page after deleting an album
    success_url = reverse_lazy("music:index")


