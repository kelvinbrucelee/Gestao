from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    return HttpResponse('Olá')
