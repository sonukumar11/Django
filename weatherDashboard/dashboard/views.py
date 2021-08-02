from dashboard.forms import CityForm
from django.http.response import HttpResponse
from django.shortcuts import render
import requests
from .models import City
from django.conf import settings
# Create your views here.



def get_weather_data(city_name):

    url = 'https://api.openweathermap.org/data/2.5/weather'
    print(city_name)
    params = {
                'q': city_name,
                'appid':  settings.OWM_API_KEY,
                'units':'metric',
            }        
    response = requests.get(url,params=params)
    json_response = response.json()
    print(response)        
    weather_data = {
                'temperature':json_response['main']['temp'],
                'temp_min':json_response['main']['temp_min'],
                'temp_max':json_response['main']['temp_max'],
                'city_name':json_response['name'],
                'country':json_response['sys']['country'],
                'lat':json_response['coord']['lat'],
                'lon':json_response['coord']['lon'],
                'weather':json_response['weather'][0]['main'],
                'weather_desc':json_response['weather'][0]['description'],
                'pressure':json_response['main']['pressure'],
                'humidity':json_response['main']['humidity'],
                'wind_speed':json_response['wind']['speed'],
            }
    return weather_data

def home(request):
    form = CityForm()
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = request.POST.get('city_name')
            weather_data = get_weather_data(city_name)
            form.save()
            #city_name = form.cleaned_data.get('city_name')
            
            
            
    elif request.method == "GET":
        city_name = City.objects.latest('date_added').city_name
        weather_data = get_weather_data(city_name)

    context = {'form':form,'weather_data':weather_data}
    return render(request,'dashboard/home.html',context=context)
