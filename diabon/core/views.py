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
	foo = ''
	return render_to_response('mon-menu.html', {'foo': foo})

def catalogue(request):
	return render_to_response('catalogue.html')

'''def aliment_details(request, category, slug):
	aliment = Food.objects.get(slug=slug)
	category = aliment.category
	System.out(category)
	return render_to_response('aliment_details.html', {'category':category, 'aliment': aliment})'''

def aliment_details(request, slug):
	aliment = Food.objects.get(slug=slug)	
	return render_to_response('aliment_details.html', {'aliment': aliment})	



# ______________________________________________ aliments details ____________________________________________

def pain(request):
	aliments = Food.objects.filter(category_id='1')
	category = 'Pains, biscottes, céréales, viennoiseries'
	return render_to_response('sub_content/aliments/sortedFood.html',{'aliments':aliments, 'category':category})

def feculents(request):
	aliments = Food.objects.filter(category_id='2')
	category = 'Féculents et légumes secs'
	return render_to_response('sub_content/aliments/sortedFood.html',{'aliments':aliments, 'category':category})

def legumes(request):
	category = 'Légumes'
	aliments = Food.objects.filter(category_id='3')
	return render_to_response('sub_content/aliments/sortedFood.html',{'aliments':aliments, 'category':category})

def fruits(request):
	category = 'Fruits et fruits secs'
	aliments = Food.objects.filter(category_id='4')
	return render_to_response('sub_content/aliments/sortedFood.html',{'aliments':aliments, 'category':category})

def produits_laitiers(request):
	category = 'produits laitiers'
	aliments = Food.objects.filter(category_id='5')
	return render_to_response('sub_content/aliments/sortedFood.html',{'aliments':aliments, 'category':category})

def plats_cuisines(request):
	category = 'Plats cuisinés'
	aliments = Food.objects.filter(category_id='6')
	return render_to_response('sub_content/aliments/sortedFood.html',{'aliments':aliments, 'category':category})

def dessert(request):
	category = 'Désserts'
	aliments = Food.objects.filter(category_id='7')
	return render_to_response('sub_content/aliments/sortedFood.html',{'aliments':aliments, 'category':category})

def confiseries(request):
	category = 'Produits sucrés, confiseries'
	aliments = Food.objects.filter(category_id='8')
	return render_to_response('sub_content/aliments/sortedFood.html',{'aliments':aliments, 'category':category})

def aperitifs(request):
	category = 'Apéritifs'
	aliments = Food.objects.filter(category_id='9')
	return render_to_response('sub_content/aliments/sortedFood.html',{'aliments':aliments, 'category':category})

def restauration_rapide(request):
	category = 'Restauration rapide'
	aliments = Food.objects.filter(category_id='11')
	return render_to_response('sub_content/aliments/sortedFood.html',{'aliments':aliments, 'category':category})

def boissons(request):
	category = 'Boissons'
	aliments = Food.objects.filter(category_id='10')
	return render_to_response('sub_content/aliments/sortedFood.html',{'aliments':aliments, 'category':category})

def sauces(request):
	category = 'Sauces, assaisonnements'
	aliments = Food.objects.filter(category_id='12')	
	return render_to_response('sub_content/aliments/sortedFood.html',{'aliments':aliments, 'category':category})



# ________________________________________________ CONSEILS ______________________________________________

def conseils(request):
	return render_to_response('conseils.html')

def article_details(request, slug):
	article = Article.objects.get(slug=slug)	
	return render_to_response('article_details.html', {'article': article})



# ________________________________________________ CONTACT ______________________________________________

def contact(request):
	foo = ''
	return render_to_response('contact.html', {'foo': foo})

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
	foo = ''
	return render_to_response('profil.html', {'foo': foo})



# ____________________________________________ MENTIONS LEGALES ________________________________________

def mentions(request):
	foo = ''
	return render_to_response('mentions-legales.html', {'foo': foo})



# ________________________________________________ L'EQUIPE ______________________________________________

def equipe(request):
	foo = ''
	return render_to_response('equipe.html', {'foo': foo})	
