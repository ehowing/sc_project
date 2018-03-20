#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from .models import Post

from django.views.generic import ListView

#import request
# from . import urls

# Create your views here.


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'



# def index(request):
#     return HttpResponse('Hello World!')
#
# def test(request):
#     return HttpResponse('My second view!')
