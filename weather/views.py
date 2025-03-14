from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import City, CityWeathers
from django.http import Http404
from weather.helper_functions.weathers import get_temperature
from django.urls import reverse
from django.utils import timezone



def index(request):
    cities = City.objects.all()
    context = {"cities": cities}
    return render(request=request, template_name="weathers/cities.html", context=context)

def detail(request, pk):
    try:
        city = City.objects.get(pk=pk)
        temperature = get_temperature(city_id=city.id)
    except City.DoesNotExist:
        city = None
        temperature = None

    context = {
        "city": city,
        "temperature": temperature
    }

    city_weathers = CityWeathers.objects.create(city=city, temperature=temperature)
    city_weathers.save()
    return render(request=request, template_name="weathers/city.html", context=context)


def weathers(request):
    city_weathers = CityWeathers.objects.all()
    context = {"city_weathers": city_weathers}
    return render(request=request, template_name="weathers/weathers.html", context=context)

def add_city(request):
    if request.method == "POST":
        city = City.objects.create(
            name=request.POST["city"],
            country = request.POST["country"],
            coordination_x=request.POST["coordination_x"],
            coordination_y = request.POST["coordination_y"]
        )
        city.save()
        return HttpResponseRedirect(reverse("weathers:cities"))
    context = {}
    return render(request=request, template_name="weathers/city_add.html", context=context)

def delete_city(request, city_id):
    city = get_object_or_404(City, id=city_id)
    city.delete()
    return HttpResponseRedirect(reverse("weathers:cities"))

# def add_city_1(request):
#     if request.method == "POST":
#         form = NameForm(request.POST)
#         if form.is_valid():
#             city = City.objects.create(
#                 name=form.cleaned_data["city"],
#                 country = form.cleaned_data["country"],
#                 coordination_x = form.cleaned_data["coordination_x"],
#                 coordination_y = form.cleaned_data["coordination_y"]
#             )
#             city.save()
#             return HttpResponseRedirect(reverse("weathers:cities"))
#
#     else:
#         form = NameForm()
#     context = {"form": form}
#     return render(request=request, template_name="weathers/city_add_1.html", context=context)
