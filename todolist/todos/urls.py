from django.conf.urls import url
from django.urls import path
from django.urls.conf import include

from . import views


urlpatterns = [
    path('', views.index,name='index'),
    url(r'^details/(?P<id>\w{0,50})/$', views.details,name='details'),
    url(r'^add', views.add,name='add'),
]

