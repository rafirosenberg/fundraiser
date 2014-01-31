from django.http import HttpResponse
from django.shortcuts import render
import json

from pledges.models import Pledge


def index(request):
    pledges = Pledge.objects.all()
    total = sum([p.amount for p in pledges])
    context = {'pledges': pledges, "total": total}
    return render(request, 'event/index.html', context)


def updateTotal(request):
    pledges = Pledge.objects.all()
    total = sum([p.amount for p in pledges])
    return HttpResponse(total)

def updateRecent(request):
    recentPledges = Pledge.objects.all()[:3]
    context = {"pledges": recentPledges}
    return render(request, 'event/pledges.html', context)

def updateTop(request):
    topPledges = Pledge.objects.all().order_by('amount').reverse()[:3]
    context = {"pledges": topPledges}
    return render(request, 'event/top_pledges.html', context)
