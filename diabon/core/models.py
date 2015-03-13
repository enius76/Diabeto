from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200)
	def __unicode__(self):
		return "%s %s" % (self.name)

class Food(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200)
	weight = models.IntegerField()
	glucide = models.FloatField()
	category = models.ForeignKey('Category')
	def __unicode__(self):
		return "%s" % (self.name)

class Profile(models.Model):
	user = models.OneToOneField(User)
	birth = models.DateField()
	sexe = models.CharField(max_length=1)
	weight = models.FloatField()
	height = models.FloatField()
	glyc = models.ForeignKey('Glyc')

	def __str__(self):
		return "Profil de {0}".format(self.user.username)

	def create_user(self, email, password=None):
	#Creates and saves a User with the given email and password.

		if not email:
			raise ValueError('Vous devez avoir une adresse mail')

		user = self.model(
			email=self.normalize_email(email),
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

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