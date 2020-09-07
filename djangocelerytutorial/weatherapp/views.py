from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from .forms import CityForm
from .models import City
from .tasks import task_get_weather_periodic


def home(request, *args, **kwargs):
    if request.method == 'POST':
        form = CityForm(request.POST)
        cities_db = City.objects.order_by('updated').reverse()
        if form.is_valid():
            form.get_weather_data()
            render(request, '../templates/cities.html', {'cities': cities_db, 'form': form})
    else:
        form = CityForm()
        cities_db = City.objects.order_by('updated').reverse()
    return render(request, '../templates/cities.html', {'cities': cities_db, 'form': form})
