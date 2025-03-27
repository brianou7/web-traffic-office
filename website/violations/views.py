from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from .models import Infraction, Violation


def index(request):
    return render(request, 'violations/index.html', {})


class ViolationListView(ListView):

    model = Violation

    def get_queryset(self):
        search = self.request.GET.get('search')
        qs = super().get_queryset().filter(vehicle__owner=self.request.user)

        if search:
            return qs.filter(
                Q(infraction__description__icontains=search) |
                Q(infraction__code__icontains=search)
            )

        return qs


class InfractionListView(ListView):

    model = Infraction

    def get_queryset(self):
        search = self.request.GET.get('search')

        if search:
            return super().get_queryset().filter(
                Q(description__icontains=search) |
                Q(code__icontains=search)
            )

        return super().get_queryset()