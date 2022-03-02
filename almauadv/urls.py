from django.contrib import admin 
from django.http import HttpRequest, HttpResponse  
from django.urls import path  
from app.views_cars import (
    index,
    delete,
    add_car,
)

from app.views_trips import (
    car_trips,
    car_trips_delete
)

urlpatterns = [
    path('', index),
    path('delete/<str:id_>', delete),
    path('add_car/', add_car),
    path('cars/<int:car_id>/trips', car_trips),
    path('delete_trip/<int:trip_id>', car_trips_delete),
    path('admin/', admin.site.urls),
]