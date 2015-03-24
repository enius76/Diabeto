# coding: utf-8
from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from datetime import datetime


class Food(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200)
	weight = models.IntegerField()
	glucide = models.FloatField()
	category = models.ForeignKey('Category')
	def __unicode__(self):
		return "%s" % (self.name)

class Category(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)
	def __unicode__(self):
		return "%s" % (self.name)

class Glyc(models.Model):
	id_user= models.AutoField(primary_key=True)
	value = models.FloatField()
	time = models.DateTimeField(default=datetime.now())
	note = models.CharField(max_length=150, default=' ')

	def __unicode__(self):
		return "%s" % (self.value)

class Profile(models.Model):
	user = models.OneToOneField(User)
	birth = models.DateField(default=datetime.now())
	sexe = models.CharField(max_length=1)
	weight = models.FloatField(default=0.0)
	height = models.FloatField(default=0.0)
	# picture = models.FileField(upload_to='/static/images/user/')
	typeDiabete = models.CharField(max_length=50)
	glycMoyenne = models.IntegerField(default=0)


	def __unicode__(self):
		return "Profile de %s" % self.user

	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)

	post_save.connect(create_user_profile, sender=settings.AUTH_USER_MODEL)

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

# ______________________________________ ARTICLES _______________________________________

class Article(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=42)
	content= models.TextField(null=True)
	date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
	slug = models.SlugField(max_length=100, default='null')
	category_article = models.ForeignKey('Categoryarticle')
	def __unicode__(self):
		return self.titre

class Categoryarticle(models.Model):
	name = models.CharField(max_length=30)
	slug = models.SlugField(max_length=30)
	def __unicode__(self):
		return "%s" % (self.name)
