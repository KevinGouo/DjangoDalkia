from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# For HTTP requests

def index(response):
    return HttpResponse("<h1> Test Django Database")


def v1(response):
    return HttpResponse("<h1>View 1")
