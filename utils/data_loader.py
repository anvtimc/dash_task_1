import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")


def load_data(city):
    response = requests.get(API_URL, params={'key': API_KEY, 'q': city, 'days': 1, 'aqi': 'yes'})
    data = response.json()
    city_name = data['location']['name']
    temp = data['current']['temp_c']
    condition = data['current']['condition']['text']
    icon = data['current']['condition']['icon']
    air = data['current']['air_quality']
    last_updated = data['current']['last_updated']

    co = air['co']
    no2 = air['no2']
    o3 = air['o3']
    so2 = air['so2']
    pm25 = air['pm2_5']
    pm10 = air['pm10']

    forecast_hours = data['forecast']['forecastday'][0]['hour']
    hours = [hour['time'][-5:] for hour in forecast_hours]
    temps = [hour['temp_c'] for hour in forecast_hours]
    ap = [hour['pressure_mb'] * 0.75 for hour in forecast_hours]
    wind = [hour['wind_kph'] / 3.6 for hour in forecast_hours]
    wind_dirs = [hour['wind_degree'] for hour in forecast_hours]
    
    co_hours = [hour['air_quality']['co'] for hour in forecast_hours]
    no2_hours = [hour['air_quality']['no2'] for hour in forecast_hours]
    o3_hours = [hour['air_quality']['o3'] for hour in forecast_hours]
    so2_hours = [hour['air_quality']['so2'] for hour in forecast_hours]
    pm25_hours = [hour['air_quality']['pm2_5'] for hour in forecast_hours]
    pm10_hours = [hour['air_quality']['pm10'] for hour in forecast_hours]

    return {
        'city_name': city_name,
        'temp': temp,
        'condition': condition,
        'icon': icon,
        'temps': temps,
        'ap': ap,
        'wind': wind,
        'wind_dirs': wind_dirs,
        'hours': hours,
        'last_updated': last_updated,
        'co': co,
        'no2': no2,
        'o3': o3,
        'so2': so2,
        'pm25': pm25,
        'pm10': pm10,
        'co_hours': co_hours,
        'no2_hours': no2_hours,
        'o3_hours': o3_hours,
        'so2_hours': so2_hours,
        'pm25_hours': pm25_hours,
        'pm10_hours': pm10_hours
    }
