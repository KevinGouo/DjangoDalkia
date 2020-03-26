from django.shortcuts import render
from django.http import Httpresponse


# Create your views here.
# For HTTP requests

def index(response):
    return Httpresponse("<h1>Test Djange Database<\h1>")