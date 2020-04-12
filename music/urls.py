from django.conf.urls import url
from . import views
from django.urls import re_path

# added lesson 21 to specify which app the detail keywords' url belongs to
app_name = 'music'

urlpatterns = [
    # L29 create homepage ^'$', reference to class IndexView,then call function as_view, then name
    re_path(r'^$', views.IndexView.as_view(), name='index'),


    # L29 /music/<primary key>/ reference to class DetailView, then call function as_view, then name
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # L30 redirect path /music/album/add reference to class AlbumCreate,then call function as_view, then name album_add
    re_path(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # L32 redirect path- /music/album/ then the catcher (?P<pk>[0-9]+) for the<primary key>
    # class (function) name as a view, then we name it album-update
    re_path(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    # L32 redirect path - /music/album/delete,  then the catcher (?P<pk>[0-9]+) for the<primary key>,
    # then we delete it, class (function) name as a view, then we name it album-delete
    re_path(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

    # L36 path to /register/ reference to class UserFormView,then call function as_view, then name register
    re_path(r'register/$', views.UserFormView.as_view(), name='register'),

]












