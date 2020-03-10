from django.conf.urls import url
from . import views
from django.urls import path
from django.urls import re_path

# added lesson 21 to specify which app the detail keywords' url belongs to
app_name = 'music'

urlpatterns = [
    # create homepage ^'$', what to do 'views.index', not required give it a name
    url(r'^$', views.index, name='index'),

    # create music sub-page using an ID /music/<ID>/
    # connect to views.py, views.detail no need for parentheses on detail
    # name it the same as the function for possible later use

    #This is the old way of doing it, depreciated;   before django 2.0, but is what is covered Tutorial 12

    #url(r"^(?P<album_id>[0-9]+)/$", views.detail, name='detail'),
    #url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    #url(r'^(\d+)/$', views.detail, name='detail'),
    #url(r'^(?P<album_id>[0-9]+)\/$', views.detail, nameth='detail'),
    #url(r'^(\d+)/$', views.detail, name='detail')

    # found this in the comments area of lesson 12
    #path('<album_id>'',views.detail, name = ''detail'),
    #path('<int:album_id>/', views.detail, name="detail"),
    #path('<int:album_id>', views.detail, name='detail'),
    #path('<int:album_id>', views.detail, name='detail'),

    # /music/<album_id>/
    re_path(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    # added lesson 22 /music/<album_id>/favorite/, for favorite selection buttons on music/<album_id> details page
    re_path(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

]








