from django.shortcuts import *
from django.shortcuts import render_to_response
import datetime
from core.models import *


def home(request):
	
	return render_to_response('home.html')

def carnet(request):
	foo = 'Test Conseils'
	return render_to_response('carnet.html', {'foo': foo})


	
def alimentation(request):
	
	return render_to_response('alimentation.html')

def conseils(request):
	foo = 'Test Conseils'
	return render_to_response('conseils.html', {'foo': foo})


def aliment_details(request, slug):
	aliment = Food.objects.get(slug=slug)	
	return render_to_response('aliment_details.html', {'aliment': aliment})	


def carnet(request):
    if request.method == 'POST':
        form = GlycForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/carnet/') 
    else:
        form = GlycForm() 

    return render_to_response('carnet.html', {'form': form,}, context_instance=RequestContext(request))

def catalogue(request):
	aliments = Food.objects.all()
	#aliments = Food.objects.filter(name__istartswith=letter) #aliments commancant par a
	return render_to_response('catalogue.html',{'aliments':aliments})

def contact(request):
	foo = ''
	return render_to_response('contact.html', {'foo': foo})


def profil(request):
	foo = ''
	return render_to_response('profil.html', {'foo': foo})


def mentions(request):
	foo = ''
	return render_to_response('mentions-legales.html', {'foo': foo})

def equipe(request):
	foo = ''
	return render_to_response('equipe.html', {'foo': foo})	

def menu(request):
	foo = ''
	return render_to_response('mon-menu.html', {'foo': foo})	

def connexion(request):
    foo = ''
    return render_to_response('connexion.html', {'foo': foo})

def inscription(request):
    foo = ''
    return render_to_response('inscription.html', {'foo': foo})

def inscription_details(request):
    foo = ''
    return render_to_response('inscription-details.html', {'foo': foo})