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
