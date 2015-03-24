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

'''class FoodViewSet(generics.ListAPIView):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	# queryset = Food.objects.all()
	serializer_class = FoodSerializer
	def get_queryset(self):
		"""
		Optionally restricts the returned purchases to a given user,
		by filtering against a `username` query parameter in the URL.
		"""
		queryset = Food.objects.all()
		category_id = self.request.QUERY_PARAMS.get('category_id', None)
		if category_id is not None:
			queryset = queryset.filter(purchaser__category_id=category_id)
		return queryset'''

'''class PainsViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows Pains to be viewed or edited.
	"""
	queryset = Food.objects.filter(category_id='1')
	serializer_class = PainsSerializer


class FeculentsViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows Feculents to be viewed or edited.
	"""
	queryset = Food.objects.filter(category_id='2')
	serializer_class = FeculentsSerializer


class LegumesViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows Legumes to be viewed or edited.
	"""
	queryset = Food.objects.filter(category_id='3')
	serializer_class = LegumesSerializer


class AperitifsViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows aperitifs to be viewed or edited.
	"""
	queryset = Food.objects.filter(category_id='9')
	serializer_class = AperitifsSerializer'''
