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
