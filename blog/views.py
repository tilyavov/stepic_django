from django.shortcuts import render


def index(request):
    return render(request, "blog/index.html")


def user(request):
    data = ['Павел', 45, '+79234567891', 'pavel@pavel.com']
    return render(request, "blog/users.html", context={'item': data})