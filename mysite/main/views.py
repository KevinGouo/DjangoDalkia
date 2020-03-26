from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# For HTTP requests

def index(response):
    return HttpResponse("<h1>Test Djange Database<\h1>")


def v1(response):
    return HttpResponse("<h1>View 1<\h1>")
