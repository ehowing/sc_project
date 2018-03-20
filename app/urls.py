# app/urls.py

# from django.conf.urls import url
#
# from app.views import index
#
# urlpatterns = [
#   url(r'^$', index, name='index'),
# ]

# from django.conf.urls import url
#
# from app.views import index
#
# urlpatterns = [
#   url(r'^$', index, name='index'),
# ]

from app.views import *
from django.conf.urls import url
from django.urls import path
#just added
from . import views

urlpatterns = [
#    ' ',
    #url(r'^$', index, name='index'),
    #url(r'^test/$', test, name='test'),
    #just added
    path('', views.HomePageView.as_view(), name='home'),

]
