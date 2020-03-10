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



]








