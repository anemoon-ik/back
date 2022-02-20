from django.http import HttpRequest, HttpResponse, HttpResponseNotFound 
from django.shortcuts import render, redirect  
from django.contrib.auth.models import User  

from app.models import Car


def index(request: HttpRequest) -> HttpResponse:
    catalog = Car.objects.all()
    return render(request, "index.html", context={
        "cars": catalog
    })


def delete(request: HttpRequest, id_: str) -> HttpResponse:
    global cars
    Car.objects.get(id=id_).delete()
    return HttpResponse("", status=204)


def add_car(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        Car.objects.create(
            model=request.POST.get("model", ""),
            speed=int(request.POST.get("speed", "")),
            color=request.POST.get("color", ""),
        )
    return redirect("/")

def edit(request: HttpRequest, id_:str) -> HttpResponse:
    try:
        car = Car.objects.get(id=id_)

        if request.method == "POST":
            car.model=request.POST.get("model", "")
            car.speed=int(request.POST.get("speed", ""))
            car.color=request.POST.get("color", "")
            car.save()
            return redirect("/")
        else:
            return render(request, "edit.html", {"car": car})
    except Car.DoesNotExist:
        return HttpResponseNotFound("<h3>Car is not found</h3>")
