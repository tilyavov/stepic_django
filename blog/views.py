from django.shortcuts import render
from django.http import HttpResponse

def index1(request):
    return HttpResponse('Hello 1')

def index2(request):
    return HttpResponse('Hello 2')

def index3(request):
    return HttpResponse('Hello 3')