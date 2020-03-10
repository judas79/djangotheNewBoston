from django.views import generic
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

