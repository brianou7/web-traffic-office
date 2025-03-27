from django.db.models import Q
from django.shortcuts import render

from .models import Vehicle


def index(request):
    search = request.GET.get('search')
    vehicles = Vehicle.objects.filter(owner=request.user)

    if search:
        vehicles = vehicles.filter(
            Q(license_plate__icontains=search) |
            Q(type__icontains=search) |
            Q(brand__icontains=search) |
            Q(model__icontains=search)
        )

    return render(request, 'vehicles/index.html', {'vehicles': vehicles})
