from django.shortcuts import render, get_list_or_404
from django.db.models import Q
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib import messages

from cars_project.config_pagination import pagination

from .models import Car


# TODO: Make it using ListView
def car_list(request):
    template = 'index.html'
    object_list = Car.objects.all()

    pages = pagination(request, object_list, 2)

    context = {
        'items': pages[0],
        'page_range': pages[1],
    }
    return render(request, template, context)


# TODO: Make it using DetailView
def car_detail(request, slug):
    template = 'cars/car.html'
    car = get_list_or_404(Car, slug=slug)
    context = {
        'car': car
    }
    return render(request, template, context)


# TODO: API is not working now. But if you need it'll work!

def search(request):
    template = 'index.html'

    query = request.GET.get('q')

    if query:
        results = Car.objects.filter(
            Q(brand__icontains=query) |
            Q(model__icontains=query)
        )
    else:
        results = Car.objects.all()

    pages = pagination(request, results, num=1)

    context = {
        'items': pages[0],
        'page_range': pages[1],
        'query': query,
    }
    return render(request, template, context)
