from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    name_is_company = ['Tajiairnavigation', 'SomonAir']
    carscompany = 'Audi'
    context = {
        'company': name_is_company,
        'car': carscompany
    }
    return render(request, 'blog/index.html', context)

