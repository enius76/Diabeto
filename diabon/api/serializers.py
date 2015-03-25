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

# ------ Food ------

class CategorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Category
		fields = ('name', 'slug')		

class FoodSerializer(serializers.HyperlinkedModelSerializer):
	category = CategorySerializer()
	class Meta:
		model = Food
		fields = ('id','name', 'weight', 'glucide', 'category')


# ------ Article ------


class ArticleCategorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Categoryarticle
		fields = ('name', 'slug')

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
	category_article = ArticleCategorySerializer()
	class Meta:
		model = Article
		fields = ('id','title', 'author', 'content', 'date', 'slug', 'category_article')
