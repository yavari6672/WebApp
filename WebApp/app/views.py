from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("home")


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
