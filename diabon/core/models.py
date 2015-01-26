from django.db import models
from django import forms
from django.forms import ModelForm

class Category(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200)
	def __unicode__(self):
		return "%s %s" % (self.name)

class Food(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200)
	weight = models.IntegerField()
	glucide = models.IntegerField()
	category = models.ForeignKey('Category')
	def __unicode__(self):
		return "%s" % (self.name)

class User(models.Model):
	name = models.CharField(max_length=150)
	firstname = models.CharField(max_length=150)
	birth = models.DateField()
	sexe = models.CharField(max_length=1)
	weight = models.IntegerField()
	height = models.IntegerField()

	mail = models.EmailField()
	password = models.CharField(max_length=8)

	glyc = models.ForeignKey('Glyc')

	def __unicode__(self):
		return "%s" % (self.name)

class Glyc(models.Model):
	value = models.FloatField()
	#time = models.DateTimeField()
	note = models.CharField(max_length=150, default=' ')

	def __unicode__(self):
		return "%s" % (self.value)

class GlycForm(ModelForm):
    class Meta:
    	model = Glyc
    	fields = ['value', 'note']