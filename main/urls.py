from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = "home"),
    path('about', views.about, name = "about"),
    path('catalog', views.catalog, name = "catalog"),
    path('contact', views.contact, name = "contact")
]
