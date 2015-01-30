from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'core.views.home', name='home'),
	url(r'^carnet-de-bord/$', 'core.views.carnet', name='carnet'),
	url(r'^alimentation/$', 'core.views.alimentation', name='alimentation'),
	url(r'^conseils/$', 'core.views.conseils', name='conseils'),
	url(r'^aliment/(?P<slug>[\w-]+)/$', 'core.views.aliment_details', name='alimentdetails'),
	url(r'^profil/$', 'core.views.profil', name='profil'),
	url(r'^contact/$', 'core.views.contact', name='contact'),
	url(r'^alimentation/catalogue/$', 'core.views.catalogue', name='catalogue'),
	url(r'^alimentation/catalogue/(?P<category>[\w-]+)/$', 'core.views.catalogue', name='catalogueCategory'),
	url(r'^alimentation/catalogue/(?P<letter>[\w-]+)/$', 'core.views.catalogue', name='catalogueLetter'),
	url(r'^alimention/mon-menu/$', 'core.views.menu', name='menu'),
	url(r'^mentions-legales/$', 'core.views.mentions', name='mentions'),
	url(r'^equipe/$', 'core.views.equipe', name='equipe'),
)