from django.contrib import admin 
from django.http import HttpRequest, HttpResponse  
from django.urls import path  
from app.views import (
    index,
    delete,
    add_car,
    edit
)

urlpatterns = [
    path('', index),
    path('delete/<str:id_>', delete),
    path('edit/<str:id_>', edit),
    path('add_car/', add_car),
    path('admin777/', admin.site.urls),
]