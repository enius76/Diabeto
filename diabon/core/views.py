# coding: utf-8

from django.shortcuts import *
from django.shortcuts import render_to_response
import datetime
from core.models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render
from django.core.urlresolvers import reverse
from core.forms import *
from django.contrib.auth.decorators import login_required



def home(request):
	return render_to_response('home.html')


@login_required
def carnet(request):
	return render_to_response('carnet.html')


def alimentation(request):
	
	return render_to_response('alimentation.html')


def conseils(request):
	return render_to_response('conseils.html')

def article_details(request):
	return render_to_response('article-details.html')


def aliment_details(request, slug):
	aliment = Food.objects.get(slug=slug)	
	return render_to_response('aliment_details.html', {'aliment': aliment})	


@login_required
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
	return render_to_response('catalogue.html')


def contact(request):
	return render_to_response('contact.html')


@login_required
def profil(request):
	return render_to_response('profil.html')


def mentions(request):
	return render_to_response('mentions-legales.html')


def equipe(request):
	return render_to_response('equipe.html')	


def menu(request):
	return render_to_response('mon-menu.html')


def connexion(request):
    return render_to_response('connexion.html')


def inscription(request):
    return render_to_response('inscription.html')


def inscription_details(request):
    return render_to_response('inscription-details.html')



def pain(request):
	aliments = Food.objects.filter(category_id='1')
	category = 'Pains, biscottes, céréales, viennoiseries'
	return render_to_response('sub_content/aliments/sortedFoodSpecific.html',{'aliments':aliments, 'category':category})

def feculents(request):
	aliments = Food.objects.filter(category_id='2')
	category = 'Féculents et légumes secs'
	return render_to_response('sub_content/aliments/sortedFoodSpecific.html',{'aliments':aliments, 'category':category})

def legumes(request):
	category = 'Légumes'
	aliments = Food.objects.filter(category_id='3')
	return render_to_response('sub_content/aliments/sortedFoodSpecific.html',{'aliments':aliments, 'category':category})

def fruits(request):
	category = 'Fruits et fruits secs'
	aliments = Food.objects.filter(category_id='4')
	return render_to_response('sub_content/aliments/sortedFoodSpecific.html',{'aliments':aliments, 'category':category})

def produits_laitiers(request):
	category = 'produits laitiers'
	aliments = Food.objects.filter(category_id='5')
	return render_to_response('sub_content/aliments/sortedFoodSpecific.html',{'aliments':aliments, 'category':category})

def plats_cuisines(request):
	category = 'Plats cuisinés'
	aliments = Food.objects.filter(category_id='6')
	return render_to_response('sub_content/aliments/sortedFoodSpecific.html',{'aliments':aliments, 'category':category})

def dessert(request):
	category = 'Désserts'
	aliments = Food.objects.filter(category_id='7')
	return render_to_response('sub_content/aliments/sortedFoodSpecific.html',{'aliments':aliments, 'category':category})

def confiseries(request):
	category = 'Produits sucrés, confiseries'
	aliments = Food.objects.filter(category_id='8')
	return render_to_response('sub_content/aliments/sortedFoodSpecific.html',{'aliments':aliments, 'category':category})

def aperitifs(request):
	category = 'Apéritifs'
	aliments = Food.objects.filter(category_id='9')
	return render_to_response('sub_content/aliments/sortedFoodSpecific.html',{'aliments':aliments, 'category':category})

def restauration_rapide(request):
	category = 'Restauration rapide'
	aliments = Food.objects.filter(category_id='11')
	return render_to_response('sub_content/aliments/sortedFoodSpecific.html',{'aliments':aliments, 'category':category})

def boissons(request):
	category = 'Boissons'
	aliments = Food.objects.filter(category_id='10')
	return render_to_response('sub_content/aliments/sortedFoodSpecific.html',{'aliments':aliments, 'category':category})

def sauces(request):
	category = 'Sauces, assaisonnements'
	aliments = Food.objects.filter(category_id='12')	
	return render_to_response('sub_content/aliments/sortedFoodSpecific.html',{'aliments':aliments, 'category':category})

def letterSort(request, letter):
	aliments = Food.objects.filter(name__istartswith=letter)
	return render_to_response('sub_content/aliments/sortedFoodSpecific.html', {'aliments': aliments})

def letterSortByCategory(request, letter, category):
	if category == "pains-biscottes-cereales-viennoiseries":
		cat = 1
	elif category == "feculents-et-legumes-secs":
		cat = 2
	elif category == "legumes":
		cat = 3
	elif category == "fruits-et-fruits-secs":
		cat = 4
	elif category == "produits-laitiers":
		cat = 5
	elif category == "plats-cuisines":
		cat = 6
	elif category == "dessert":
		cat = 7
	elif category == "produits-sucres-confiseries":
		cat = 8
	elif category == "aperitifs":
		cat = 9
	elif category == "restauration-rapide":
		cat = 11
	elif category == "boissons":
		cat = 10
	elif category == "sauces-assaisonnements":
		cat = 12

	aliments = Food.objects.filter(category_id = cat).filter(name__istartswith=letter)
	return render_to_response('sub_content/aliments/sortedFoodSpecific.html', {'aliments': aliments, 'category':category})

def connexion(request):
	error = False

	if request.method == "POST":
		form = ConnexionForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
			if user:  # Si l'objet renvoyé n'est pas None
				login(request, user)  # nous connectons l'utilisateur
				return redirect('carnet')
			else: # sinon une erreur sera affichée
				error = True
	else:
		form = ConnexionForm()

	return render(request, 'connexion.html', locals())

def deconnexion(request):
	logout(request)
	#return redirect(reverse(connexion))
	return HttpResponseRedirect('/')

def inscription(request):
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
			return HttpResponseRedirect('/inscription-complete')
	else:
		form = RegistrationForm()
	variables = RequestContext(request, {
	'form': form
	})
	return render_to_response(
	'inscription.html',
	variables,
	)

def inscriptionComplete(request):
	return render_to_response('merci.html')
