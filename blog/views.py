from django.http import HttpResponse


def index(request):
    return HttpResponse("Главная страница")


def user(request):
    name = request.GET.get("name")
    age = request.GET.get("age")
    return HttpResponse(f"<h2>Имя: {name}, Возраст: {age}</h2>")