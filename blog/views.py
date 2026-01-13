from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest

def index(request, id):
    people = [None, 'Sam', 'Bob']
    if id in range(len(people)):
        return HttpResponse(people[id])
    else:
        return HttpResponseNotFound('Not Found')

def access(request, age):
    if age not in range(1,111):
        return HttpResponseBadRequest('Некорректные данные')
    elif age > 17:
        return HttpResponse('Доступ разрешён')
    else:
        return HttpResponseForbidden('Доступ заблокирован: недостаточно лет')