from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from .models import App


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def app_list(request):
    apps = App.objects.all().values()
    template = loader.get_template('app_list.html')
    context = {
        'apps': apps,
    }
    return HttpResponse(template.render(context, request))
