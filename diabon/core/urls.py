# coding: utf-8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'core.views.home', name='home'),
	url(r'^carnet-de-bord/$', 'core.views.carnet', name='carnet'),

	url(r'^profil/$', 'core.views.profil', name='profil'),
	url(r'^contact/$', 'core.views.contact', name='contact'),

	url(r'^mentions-legales/$', 'core.views.mentions', name='mentions'),
	url(r'^equipe/$', 'core.views.equipe', name='equipe'),
	url(r'^connexion/$', 'core.views.connexion', name='connexion'),
	url(r'^deconnexion$', 'core.views.deconnexion', name='deconnexion'),
	url(r'^inscription/$', 'core.views.inscription', name='inscription'),
	url(r'^inscription-details/$', 'core.views.inscription_details', name='inscription-details'),
	url(r'^inscription-complete/$', 'core.views.inscriptionComplete', name='inscriptionComplete'),

	url(r'^aliment/(?P<slug>[\w-]+)/$', 'core.views.aliment_details', name='alimentdetails'),
	url(r'^alimentation/$', 'core.views.alimentation', name='alimentation'),
	url(r'^alimentation/mon-menu/$', 'core.views.menu', name='menu'),
	url(r'^alimentation/catalogue/$', 'core.views.catalogue', name='catalogue'),
	url(r'^alimentation/catalogue/(?P<slug>[\w-]+)/$', 'core.views.category', name='category'),
	url(r'^alimentation/catalogue/lettre/(?P<letter>\w{1})/$', 'core.views.letterSort', name='letterSort'),
	url(r'^alimentation/catalogue/(?P<slug>[\w-]+)/lettre/(?P<letter>\w{1})/$', 'core.views.letterSortByCategory', name='letterSortByCategory'),

	url(r'^conseils/$', 'core.views.conseils', name='conseils'),
	url(r'^conseils/(?P<slug>[\w-]+)/$', 'core.views.article_details', name='articledetails'),
)
