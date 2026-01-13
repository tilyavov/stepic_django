from django.urls import path
from blog import views

urlpatterns = [
    path("", views.index),
    path("contact/", views.contact),
    path("support/", views.support),
]