import django_filters
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import *
from core.models import *
from rest_framework import generics


class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Group.objects.all()
	serializer_class = GroupSerializer

class FoodViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Food.objects.all()
	serializer_class = FoodSerializer

class FoodCategory(generics.ListAPIView):

	serializer_class = FoodSerializer
	def get_queryset(self):
		queryset = Food.objects.all()
		category = self.kwargs['category']

		queryset = queryset.filter(category_id=category)
		return queryset

class ArticleViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer

class ArticleCategory(generics.ListAPIView):

	serializer_class = ArticleSerializer
	def get_queryset(self):
		queryset = Article.objects.all()
		category_article = self.kwargs['category_article']

		queryset = queryset.filter(category_article_id=category_article)
		return queryset
