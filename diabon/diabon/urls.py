from django.conf.urls import url, include
from rest_framework import routers


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    url(r'api/', include('api.urls')),
    url(r'', include('core.urls'))

]