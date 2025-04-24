from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.cars_home, name='cars_home'),
    path('create/', views.create, name='create'),
    path('my/', views.my_cars, name='my_cars'),
    path('<int:car_id>/', views.car_detail, name='car_detail'),
    path('<int:pk>/edit/', views.CarUpdateView.as_view(), name='car_edit'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]