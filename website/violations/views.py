from django.shortcuts import render
from django.views.generic import ListView

from .models import Infraction, Violation


def index(request):
    return render(request, 'violations/index.html', {})


class ViolationListView(ListView):

    model = Violation

    def get_queryset(self):
        return super().get_queryset().filter(vehicle__owner=self.request.user)


class InfractionListView(ListView):

    model = Infraction
