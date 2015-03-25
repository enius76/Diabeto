from api import views
from rest_framework import routers
from django.conf.urls import url, include, patterns
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth.models import User

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'food', views.FoodViewSet)
router.register(r'article', views.ArticleViewSet)

# router.register(r'food/$', views.FoodViewSet, 'food-list')
# router.register(r'pains-crackers-cereales-patisseries', views.PainsViewSet)
# router.register(r'feculents-legumes-secs', views.FeculentsViewSet)
# router.register(r'legumes', views.LegumesViewSet)
# router.register(r'aperitifs', views.AperitifsViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    url(r'', include(router.urls)),
    url('^foods/(?P<category>\w+)/$', views.FoodCategory.as_view()),
    url('^articles/(?P<category_article>\w+)/$', views.ArticleCategory.as_view()),
]