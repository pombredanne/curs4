from django.conf.urls import patterns, url, include
from django.conf import settings
from views import *


urlpatterns = patterns('',
    url(r'^$', logout, name="logout"),
    url(r'register/$', register, name="register"),
    
)