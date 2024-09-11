from django.shortcuts import render
from .models import Car

def home(request):
    return render(request, 'index.html')

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})

def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'car_detail.html', {'car': car})

def contact(request):
    return render(request, 'contact.html')
