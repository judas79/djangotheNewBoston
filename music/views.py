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

# L35 class to create registration form and redirect after submitting it
class UserFormView(View):

    # blueprints class name for this form
    form_class = UserForm

    # template name and path to corresponding registration form html file
    template_name = 'music/registration_form.html'

    # built in function to use get request and another function for post
    # display a blank form using form_class we created above, passed None by default(not filled out, blank)
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data by registering it, and passing to the data base
    def post(self, request):
        form = self.form_class(request.POST)

        # if Post data is valid, further do custom validation
        if form.is_valid():

            # create object 'user', do not save 'commit' it to the database
            user = form.save(commit=False)

            # cleaned(normalised) data,
            # COMMENTS AREA FIXED BY USING user.username instead of just username(lesson35 error)
            user.username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # call special function to set password, to pass in the password
            user.set_password(password)

            # save to database
            user.save()

            # returns User objects if credentials are correct
            # make variable, user, see if keywords are in data base
            user = authenticate(username=user.username, password=password)

            # if keywords are in the database
            if user is not None:

                # check to see if user has been disabled or banned
                if user.is_active:

                    # log the user in by passing in request and user
                    login(request, user)

                    # return user to main page after logging in
                    return redirect('music:index')

        # if the submission to log in fails, the process starts over with a blank form
        return render(request, self.template_name, {'form': form})


