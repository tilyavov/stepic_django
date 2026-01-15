from django.shortcuts import render


def index(request):
    return render(request, "blog/index.html")


def user(request):
    data = {'name': 'Павел', 'age': 45, 'phone': '+79234567891', 'email': 'pavel@pavel.com'}
    return render(request, "blog/users.html", context=data)