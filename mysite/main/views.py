from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# For HTTP requests

def index(response):
    return HttpResponse("<h1>%s" % id)
