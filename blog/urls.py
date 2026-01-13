from django.urls import path, include, re_path
from blog import views

product_patterns = [
    path('', views.products),
    path('comments/', views.comments),
    path('questions/', views.questions),
]

urlpatterns = [
    path('', views.index),
    path('products/<int:id>/', include(product_patterns)),
]
