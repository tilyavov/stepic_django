from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'my_name': 'Alisher',
        'my_age': 22
    }
    return render(request, 'blog/index.html', context)

