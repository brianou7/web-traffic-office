from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Owner


def index(request):
    owners = Owner.objects.all()[:5]
    return render(request, 'owners/index.html', {'owners': owners})

def detail(request, owner_id):
    owner = Owner.objects.get(pk=owner_id)
    return render(request, 'owners/detail.html', {'owner': owner})

def results(request, owner_id):
    response = 'You\'re looking at the results of question %s.'
    return HttpResponse(response % owner_id)


def vote(request, owner_id):
    return HttpResponse('You\'re voting on question %s.' % owner_id)