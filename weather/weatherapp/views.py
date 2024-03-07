from django.shortcuts import render
import requests

def weather(request):
    if request.method == 'POST':
        city_name = request.POST['city']
        api_key = '360e4bc3865e745ec844bd7ec054ca11'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()
        context = {}
        if 'name' in data:
            context = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description']
            }
        else:
            context['error_message'] = "City not found"
        return render(request, 'weather.html', context)
    else:
        error_message = "City not found"
    return render(request, 'weather.html', {'error_message': error_message})
