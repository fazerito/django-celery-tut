from django.core.paginator import Paginator
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from .forms import CityForm
from .models import City
from .tasks import task_get_weather_periodic


def home(request, *args, **kwargs):
    if request.method == 'POST':
        form = CityForm(request.POST)
        cities_db = City.objects.order_by('-updated')
        paginator = Paginator(cities_db, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        if form.is_valid():
            form.get_weather_data()
            render(request, '../templates/cities.html', {'page_obj': page_obj, 'form': form})
    else:
        form = CityForm()
        cities_db = City.objects.order_by('-updated')
        paginator = Paginator(cities_db, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    return render(request, '../templates/cities.html', {'page_obj': page_obj, 'form': form})
