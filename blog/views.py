from django.shortcuts import render


def index(request):
    return render(request, "blog/index.html")


def user(request):
    user_list = [
             {'name': 'Дмитрий', 'experience': 9},
             {'name': 'Павел',   'experience': 5},
             {'name': 'Алексей', 'experience': 3},
             {'name': 'Иван',    'experience': 0},
             {'name': 'Денис',   'experience': 2},
             {'name': 'Игорь',   'experience': 7},
             {'name': 'Руслан',  'experience': 1},
             {'name': 'Евгений', 'experience': 4},
             {'name': 'Андрей',  'experience': 2},
             {'name': 'Николай', 'experience': 8}]
    return render(request, "blog/users.html", context={'item': user_list})