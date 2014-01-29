from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

from pledges.models import Donor, Pledge


# Create your views here.
def index(request):
    pledges = Pledge.objects.all()
    context = {'pledges': pledges}
    return render(request, 'event/index.html', context)
