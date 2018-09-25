from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Event

def index(request):
    events = Event.objects.order_by('name').values()
    return JsonResponse({'data': list(events)})

def detail(request, id):
    return HttpResponse("CHUJU ZLOTY %s" % id)
