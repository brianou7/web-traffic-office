from django.shortcuts import render
from django.views.generic import ListView

from .models import Infraction, Violation


def index(request):
    return render(request, 'violations/index.html', {})


class ViolationListView(ListView):

    model = Violation


class InfractionListView(ListView):

    model = Infraction
