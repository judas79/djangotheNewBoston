from django.conf.urls import url
from . import views


urlpatterns = [
    # create homepage ^'$', what to do 'views.index', not required give it a name
    url(r'^$', views.index, name='index'),
]