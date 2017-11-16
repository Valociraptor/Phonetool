from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index), #login page
    url(r'^profile/(?P<id>\d+)', views.profile), #profile page for indiivdual users
    url(r'^awards', views.awards),
    url(r'^register', views.register),
    url(r'^login', views.login),
    url(r'^requestaward', views.requestaward),



]