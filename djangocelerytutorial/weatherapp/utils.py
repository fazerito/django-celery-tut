import requests
from datetime import datetime
from django.conf import settings
from .models import City

def get_weather_data(city='Wrocław'):
    api_key = settings.OPENWEATHER_API_KEY
    url = "http://api.openweathermap.org/data/2.5/weather?units=metric&q={}&APPID={}".format(city, api_key)
    response = requests.get(url).json()

    city = response['name']
    desc = response['weather'][0]['description']
    temp = response['main']['temp']
    temp_feels = response['main']['feels_like']
    pressure = response['main']['pressure']
    humidity = response['main']['humidity']
    timestamp = response['dt']
    country = response['sys']['country']

    data = {
        'city': city,
        'desc': desc,
        'temp': temp,
        'temp_feels': temp_feels,
        'pressure': pressure,
        'humidity': humidity,
        'timestamp': timestamp,
        'country': country
    }
    return data

def save_weather_data(city):
    if city is None:
        city = City.objects.order_by('updated')[0].name
    data = get_weather_data(city)
    city_to_save = City(
        name=data['city'],
        description=data['desc'],
        temperature=data['temp'],
        temperature_feel=data['temp_feels'],
        pressure=data['pressure'],
        humidity=data['humidity'],
        updated=datetime.fromtimestamp(data['timestamp']),
        country=data['country']
    )
    city_to_save.save()
