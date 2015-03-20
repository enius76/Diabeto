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



# _______________________________________________ CONNEXION _____________________________________________

def connexion(request):
    foo = ''
    return render_to_response('connexion.html', {'foo': foo})



# ______________________________________________ INSCRIPTION _____________________________________________

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

def inscription_details(request):
    foo = ''
    return render_to_response('inscription-details.html', {'foo': foo})



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
	return render_to_response('sub_content/aliments/sortedFoodCategory.html',{'aliments':aliments})

def letterSort(request, letter):
	aliments = Food.objects.filter(name__istartswith=letter)
	return render_to_response('sub_content/aliments/sortedFood.html', {'aliments': aliments})

def letterSortByCategory(request, letter, slug):
	aliments = Food.objects.filter(category__slug = slug).filter(name__istartswith=letter)
	cat = aliments[0]
	return render_to_response('sub_content/aliments/sortedFoodCategory.html', {'aliments': aliments, 'cat':cat})


# ________________________________________________ CONSEILS ______________________________________________

def conseils(request):
	return render_to_response('conseils.html')

def article_details(request):
	return render_to_response('article-details.html')



# ________________________________________________ CONTACT ______________________________________________

def contact(request):
	return render_to_response('contact.html')

def contact(request):
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']
			cc_myself = form.cleaned_data['cc_myself']

			recipients = ['briceberthelot64@gmail.com']
			if cc_myself:
				recipients.append(sender)

			send_mail(subject, message, sender, recipients)
			return HttpResponseRedirect('/contact-effectue/')

def contactEffectue(request):
	return render_to_response('merci.html')



# ________________________________________________ PROFIL ______________________________________________

@login_required
def profil(request):
	return render_to_response('profil.html')



# ____________________________________________ MENTIONS LEGALES ________________________________________

def mentions(request):
	return render_to_response('mentions-legales.html')



# ________________________________________________ L'EQUIPE ______________________________________________

def equipe(request):
	return render_to_response('equipe.html')	
