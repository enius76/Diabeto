from django.shortcuts import *
from django.shortcuts import render_to_response
import datetime
from core.models import *


def home(request):
	foo = 'Hello'
	return render_to_response('home.html', {'foo': foo})
	
def carnet(request):
	foo = 'Test carnet de bord'
	return render_to_response('carnet.html', {'foo': foo})
	
def alimentation(request):
	foo = 'Test Alimentation'
	return render_to_response('alimentation.html', {'foo': foo})

def conseils(request):
	foo = 'Test Conseils'
	return render_to_response('conseils.html', {'foo': foo})


def aliment_details(request, slug):
	aliment = Food.objects.get(name=name)
	return render_to_response('aliment_details.html', {'aliment': aliment})	
