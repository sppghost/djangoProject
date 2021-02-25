from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse('Hello World ! ')


def second(request):
    context = {'hello': 'Hello Spp'}
    return render(request, 'home.html', context)
