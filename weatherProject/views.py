from django.shortcuts import render
from weather.models import City
from weather.helper_functions.weathers import get_temperature


def home(request):
    cities = City.objects.all()[:4]

    # Get the temperature for each city
    city_data = []
    for city in cities:
        temperature = get_temperature(city_id=city.id)  # Get the temperature for each city
        city_data.append({
            'city': city,
            'temperature': temperature
        })

    # Pass city data to the template
    context = {
        "city_data": city_data
    }
    return render(request=request, template_name="home.html", context=context)