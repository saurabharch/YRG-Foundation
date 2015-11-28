__author__ = 'abchauhan'
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^SMS/$', views.index, name='index'),
    url(r'^email/$', views.email, name='email'),
]