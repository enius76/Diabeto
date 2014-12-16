from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'core.views.home', name='home'),
	url(r'^carnet/$', 'core.views.carnet', name='carnet'),
	url(r'^alimentation/$', 'core.views.alimentation', name='alimentation'),
	url(r'^conseils/$', 'core.views.conseils', name='conseils'),
	url(r'^aliment/(?P<name>[\w-]+)/$', 'core.views.aliment_details', name='alimentdetails'),
)