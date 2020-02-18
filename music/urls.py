from django.conf.urls import url
from . import views
from django.urls import path
from django.urls import re_path

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

    re_path(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

]








