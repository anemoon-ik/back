from django.db.models import Sum
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from app.models import (
    Car,
    Trip,
)


def car_trips(request: HttpRequest, car_id: int) -> HttpResponse:
    if request.user.is_anonymous:
        return redirect("/login")

    car = Car.objects.get(id=car_id)
    if car.user != request.user:
        return redirect("/")

    if request.method == "POST":
        print("post request", request.POST)
        if request.POST.get("id_", "") == "":
            Trip.objects.create(
                car_id=car_id,
                km=int(request.POST.get("trip_km", "0")),
                date=request.POST.get("trip_date", ""),
            )
        else:
            trip = Trip.objects.get(pk=int(request.POST.get("id_", "")))
            trip.km = int(request.POST.get("trip_km", "0"))
            trip.date = date=request.POST.get("trip_date", "")
            trip.save()
        return redirect(f"/cars/{car_id}/trips")

    context = dict()
    context["car"] = car
    trips = Trip.objects.filter(car=car)
    date_from = request.GET.get("date_from", "")
    date_to = request.GET.get("date_to", "")
    if date_from != "":
        trips = trips.filter(date__gte=date_from)
    if date_to != "":
        trips = trips.filter(date__lte=date_to)

    context["trips"] = trips
    context["date_from"] = date_from
    context["date_to"] = date_to
    context["total"] = trips.aggregate(Sum('km'))["km__sum"]
    return render(request, "trips.html", context=context)


def car_trips_delete(request: HttpRequest, trip_id: int) -> HttpResponse:
    if request.user.is_anonymous:
        return redirect("/login")

    if request.method == "DELETE":
        trip = Trip.objects.get(id=trip_id)
        if trip.car.user != request.user:
            return HttpResponse("Not authorized", status=401)
        trip.delete()
        return HttpResponse("", status=204)

    return HttpResponse("Method not allowed (only DELETE)", status=405)