from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse

def index(request):
    data = {'name': 'Дмитрий', 'age': 39, 'phone': '+79123456789', 'email': 'dmitry@email.com'}
    return TemplateResponse(request, 'blog/index.html', context = data)

