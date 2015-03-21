# coding: utf-8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'core.views.home', name='home'),
	url(r'^carnet-de-bord/$', 'core.views.carnet', name='carnet'),
	url(r'^profil/$', 'core.views.profil', name='profil'),
	url(r'^contact/$', 'core.views.contact', name='contact'),
	url(r'^contact-effectue/$', 'core.views.contactEffectue', name='contactEffectue'),

	url(r'^mentions-legales/$', 'core.views.mentions', name='mentions'),
	url(r'^equipe/$', 'core.views.equipe', name='equipe'),
	url(r'^connexion/$', 'core.views.connexion', name='connexion'),
	url(r'^deconnexion$', 'core.views.deconnexion', name='deconnexion'),
	url(r'^inscription/$', 'core.views.inscription', name='inscription'),
	url(r'^inscription-details/$', 'core.views.inscription_details', name='inscription-details'),
	url(r'^inscription-complete/$', 'core.views.inscriptionComplete', name='inscriptionComplete'),

	url(r'^alimentation/$', 'core.views.alimentation', name='alimentation'),
	url(r'^alimentation/catalogue/$', 'core.views.catalogue', name='catalogue'),
	url(r'^alimentation/mon-menu/$', 'core.views.menu', name='menu'),
	url(r'^alimentation/(?P<slug>[\w-]+)/$', 'core.views.aliment_details', name='alimentdetails'),
	url(r'^alimentation/catalogue/pains-biscottes-cereales-viennoiseries/$', 'core.views.pain', name='pain'),
	url(r'^alimentation/catalogue/feculents-et-legumes-secs/$', 'core.views.feculents', name='feculents'),
	url(r'^alimentation/catalogue/legumes/$', 'core.views.legumes', name='legumes'),
	url(r'^alimentation/catalogue/fruits-et-fruits-secs/$', 'core.views.fruits', name='fruits'),
	url(r'^alimentation/catalogue/produits-laitiers/$', 'core.views.produits_laitiers', name='produits_laitiers'),
	url(r'^alimentation/catalogue/plats-cuisines/$', 'core.views.plats_cuisines', name='plats_cuisines'),
	url(r'^alimentation/catalogue/dessert/$', 'core.views.dessert', name='dessert'),
	url(r'^alimentation/catalogue/produits-sucres-confiseries/$', 'core.views.confiseries', name='confiseries'),
	url(r'^alimentation/catalogue/aperitifs/$', 'core.views.aperitifs', name='aperitifs'),
	url(r'^alimentation/catalogue/restauration-rapide/$', 'core.views.restauration_rapide', name='restauration_rapide'),
	url(r'^alimentation/catalogue/boissons/$', 'core.views.boissons', name='boissons'),
	url(r'^alimentation/catalogue/sauces-assaisonnements/$', 'core.views.sauces', name='sauces'),
	#url(r'^alimentation/catalogue/(?P<category>[\w-]+)/(?P<slug>[\w-]+)/$', 'core.views.aliment_details', name='alimentdetails'),

	url(r'^conseils/$', 'core.views.conseils', name='conseils'),
	url(r'^conseils/(?P<slug>[\w-]+)/$', 'core.views.article_details', name='articledetails'),
)
