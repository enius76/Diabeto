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
from django.core.mail import send_mail


def home(request):
	return render_to_response('home.html')


# ______________________________________________ INSCRIPTION _____________________________________________

def inscription(request):
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(
            username=form.cleaned_data['username'],
            first_name=form.cleaned_data['firstName'],
            last_name=form.cleaned_data['lastName'],
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
	return render(request, 'merci.html', locals())

def inscription_details(request):
	if request.method == "POST":
		form = InscriptionDetailsForm(request.POST)
		if form.is_valid():
			userId = request.user.id
			userInfo =  Profile.objects.get(user_id=userId) # on recup la ligne de son profil dans 'profile'

			# recuperation des champs du form si ils sont remplis

			birth = form.cleaned_data["birth"] 
			userInfo.birth = birth

			sexe = form.cleaned_data["sexe"]
			userInfo.sexe = sexe

			height = form.cleaned_data["height"] 
			userInfo.height = height

			weight = form.cleaned_data["weight"]
			userInfo.weight = weight
			'''if picture:
			picture = request.FILES["picture"] 
			userInfo.picture = picture'''

			typeDiabete = form.cleaned_data["typeDiabete"]
			userInfo.typeDiabete = typeDiabete

			glycMoyenne = form.cleaned_data["glycMoyenne"] 
			userInfo.glycMoyenne = glycMoyenne

			# on enregistre
			userInfo.save()
			return redirect('profil')
	else:
		form = InscriptionDetailsForm()
	variables = RequestContext(request, {
	'form': form
	})
	return render_to_response(
	'inscription-details.html',
	variables,
	)

def inscription_detailsComplete(request):
	return render_to_response('merci.html')



# _____________________________________________ [DE]CONNEXION _____________________________________________

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



# _________________________________________________ CARNET _______________________________________________

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

def tois_derniers_mois(request):
	return render_to_response('3-derniers-mois.html')

# ______________________________________________ ALIMENTATION ____________________________________________


def alimentation(request):
	return render_to_response('alimentation.html')

def menu(request):
	return render_to_response('mon-menu.html')

def catalogue(request):
	return render_to_response('catalogue.html')

def aliment_details(request, slug):
	aliment = Food.objects.get(slug=slug)	
	return render_to_response('aliment_details.html', {'aliment': aliment})	


# ______________________________________________ aliments details ____________________________________________

def category(request, slug):
	aliments = Food.objects.filter(category__slug=slug)
	currentUrl = request.path
	currentUrl = currentUrl.split('/')
	currentUrl = currentUrl[3]
	return render_to_response('sub_content/aliments/sortedFoodCategory.html',{'aliments':aliments, 'currentUrl': currentUrl}, context_instance=RequestContext(request))

def letterSort(request, letter):
	aliments = Food.objects.filter(name__istartswith=letter)
	nb_aliment = len(aliments)
	return render_to_response('sub_content/aliments/sortedFood.html', {'nb_aliment':nb_aliment, 'letter':letter, 'aliments': aliments})

def letterSortByCategory(request, letter, slug):
	aliments = Food.objects.filter(category__slug = slug).filter(name__istartswith=letter)
	nb_aliment = len(aliments)
	currentUrl = request.path
	currentUrl = currentUrl.split('/')
	currentUrl = currentUrl[3]
	return render_to_response('sub_content/aliments/sortedFoodCategory.html',{'nb_aliment':nb_aliment, 'letter':letter, 'aliments':aliments, 'currentUrl': currentUrl}, context_instance=RequestContext(request))



# ________________________________________________ CONSEILS ______________________________________________

def conseils(request):
	return render_to_response('conseils.html')

def article_details(request, slug):
	article = Article.objects.get(slug=slug)	
	return render_to_response('article_details.html', {'article': article})



# ________________________________________________ CONTACT ______________________________________________

def contact(request):
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']
			recipients = ['briceberthelot64@gmail.com']
			send_mail(subject, message, sender, recipients)
			return HttpResponseRedirect('/contact-effectue/')
	else:
		form = ContactForm()
	variables = RequestContext(request, {
	'form': form
	})
	return render_to_response(
	'contact.html',
	variables,
	)	

def contactEffectue(request):
	return render_to_response('merci.html')



# ________________________________________________ PROFIL ______________________________________________

@login_required
def profil(request):
	userId = request.user.id
	profile =  Profile.objects.get(user_id=userId)
	return render_to_response('profil.html', {'profile':profile}, context_instance=RequestContext(request))



# ____________________________________________ MENTIONS LEGALES ________________________________________

def mentions(request):
	return render_to_response('mentions-legales.html')



# ________________________________________________ L'EQUIPE ______________________________________________

def equipe(request):
	return render_to_response('equipe.html')	
