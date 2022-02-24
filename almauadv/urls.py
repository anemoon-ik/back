from django.contrib import admin 
from django.http import HttpRequest, HttpResponse  
from django.urls import path  
from app.views import (
    index,
    delete,
    add_car,
    car_trips,
    add_trip
)

urlpatterns = [
    path('', index),
    path('delete/<str:id_>', delete),
    path('add_car/', add_car),
    path('cars/<int:id_>', car_trips),
    path('add_trip/', add_trip),
    path('admin777/', admin.site.urls),
]