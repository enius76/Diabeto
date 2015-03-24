from django.contrib.auth.models import User, Group
from rest_framework import serializers
from core.models import *
class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')
class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')
class CategorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Category
		fields = ('name', 'slug')		
class FoodSerializer(serializers.HyperlinkedModelSerializer):
	category = CategorySerializer()
	class Meta:
		model = Food
		fields = ('id','name', 'weight', 'glucide', 'category')

'''class PainsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Food
		fields = ('id','name', 'weight', 'glucide')

class FeculentsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Food
		fields = ('id','name', 'weight', 'glucide')

class AperitifsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Food
		fields = ('id','name', 'weight', 'glucide')

class LegumesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Food
		fields = ('id','name', 'weight', 'glucide')'''