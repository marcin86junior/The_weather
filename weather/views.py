import requests
from django.shortcuts import render
from .models import City

# Create your views here.

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=eabf7d9b80a49016347106c26138fef2&units=metric&lang=en'
    city = 'Poznan'

    cities = City.objects.all()
    weather_data = []

    for city in cities:
       r = requests.get(url.format(city)).json()
       city_weather = { 
        'city' : city.name,
        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon'],
       }

       weather_data.append(city_weather)

    print(weather_data)
    context = {'weather_data':weather_data}

    return render(request, 'weather/weather.html', context)

def indexPL(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=eabf7d9b80a49016347106c26138fef2&units=metric&lang=pl'
    city = 'Poznan'

    cities = City.objects.all()
    weather_data = []

    for city in cities:
       r = requests.get(url.format(city)).json()
       city_weather = { 
        'city' : city.name,
        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon'],
       }

       weather_data.append(city_weather)

    print(weather_data)
    context = {'weather_data':weather_data}

    return render(request, 'weather/weather.html', context)

def indexCH(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=eabf7d9b80a49016347106c26138fef2&units=metric&lang=zh_tw'
    city = 'Poznan'

    cities = City.objects.all()
    weather_data = []

    for city in cities:
       r = requests.get(url.format(city)).json()
       city_weather = { 
        'city' : city.name,
        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon'],
       }

       weather_data.append(city_weather)

    print(weather_data)
    context = {'weather_data':weather_data}

    return render(request, 'weather/weather.html', context)

def indexAR(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=eabf7d9b80a49016347106c26138fef2&units=metric&lang=ar'
    city = 'Poznan'

    cities = City.objects.all()
    weather_data = []

    for city in cities:
       r = requests.get(url.format(city)).json()
       city_weather = { 
        'city' : city.name,
        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon'],
       }

       weather_data.append(city_weather)

    print(weather_data)
    context = {'weather_data':weather_data}

    return render(request, 'weather/weather.html', context)