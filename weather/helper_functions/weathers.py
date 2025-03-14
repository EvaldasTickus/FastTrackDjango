import requests
from weather.models import City

def get_temperature(city_id):
    city = City.objects.get(id=city_id)
    url = f'https://api.open-meteo.com/v1/forecast?latitude={city.coordination_x}&longitude={city.coordination_y}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m'
    data = requests.get(url)
    json_data = data.json()
    temperature = json_data["current"]["temperature_2m"]
    return round(temperature)

