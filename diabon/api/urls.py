from api import views
from rest_framework import routers
from django.conf.urls import url, include, patterns
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'food', views.FoodViewSet)
# router.register(r'food/$', views.FoodViewSet, 'food-list')
# router.register(r'pains-crackers-cereales-patisseries', views.PainsViewSet)
# router.register(r'feculents-legumes-secs', views.FeculentsViewSet)
# router.register(r'legumes', views.LegumesViewSet)
# router.register(r'aperitifs', views.AperitifsViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^foods/(?P<category>\w+)/$', views.FoodCategory.as_view()),
]