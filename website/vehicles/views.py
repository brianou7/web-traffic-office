from django.shortcuts import render

from .models import Vehicle


def index(request):
    vehicles = Vehicle.objects.filter(owner=request.user)
    return render(request, 'vehicles/index.html', {'vehicles': vehicles})
