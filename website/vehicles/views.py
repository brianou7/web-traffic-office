from django.shortcuts import render

from .models import Vehicle


def index(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicles/index.html', {'vehicles': vehicles})
