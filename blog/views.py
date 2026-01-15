from django.shortcuts import render


def index(request):
    return render(request, "blog/index.html")


def user(request):
    data = {'name': 'pavel', 'year': 1}
    return render(request, "blog/users.html", context={'item': data})