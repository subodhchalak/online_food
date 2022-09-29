from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    message = "Hello World"
    return HttpResponse(message)