from datetime import datetime
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound 
from django.shortcuts import render, redirect  
from django.contrib.auth.models import User  

from app.models import Car, Trip


def index(request: HttpRequest) -> HttpResponse:
    catalog = Car.objects.all()
    return render(request, "index.html", context={
        "cars": catalog
    })

def trips(request: HttpRequest) -> HttpResponse:
    catalog1 = Trip.objects.all()
    return render(request, "trips.html", context={
        "trips": catalog1
    })


def delete(request: HttpRequest, id_: str) -> HttpResponse:
    global cars
    Car.objects.get(id=id_).delete()
    return HttpResponse("", status=204)


def add_car(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        if request.POST.get("id_", "") == "":
            Car.objects.create(
                model=request.POST.get("model", ""),
                speed=int(request.POST.get("speed", "")),
                color=request.POST.get("color", ""),
            )
        else:
            car = Car.objects.get(pk=int(request.POST.get("id_", "")))
            car.model = request.POST.get("model", "")
            car.speed = int(request.POST.get("speed", ""))
            car.color = request.POST.get("color", "")
            car.save()
    return redirect("/")


def add_trip(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        if request.POST.get("id_", "") == "":
            Trip.objects.create(
                date=request.POST.get("date", ""),
                km=request.POST.get("km", ""),
            )
        else:
            trip = Trip.objects.get(pk=int(request.POST.get("id_", "")))
            trip.date = request.POST.get("date", "")
            trip.km = request.POST.get("km", "")
            trip.save()
    return redirect("/")



def car_trips(request: HttpRequest, id_: int) -> HttpResponse:
    return render(request, "trips.html", {"trips": trips})