from django.urls import path, re_path
from blog import views

urlpatterns = [
    path('', views.index, name='index1'),
    path('about/', views.about, kwargs={'name': 'Tom', 'age': 22}),
    re_path(r'^contact/', views.contact),
]
