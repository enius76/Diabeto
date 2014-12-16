from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return "%s %s" % (self.name)

class Food(models.Model):
	name = models.CharField(max_length=200)
	picture = models.ImageField(upload_to="static/upload/")
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
	value = models.IntegerField()
	time = models.DateTimeField()

	def __unicode__(self):
		return "%s" % (self.value)
