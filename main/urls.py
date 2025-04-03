from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('catalog', views.catalog),
    path('contact', views.contact)
]
