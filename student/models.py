from django.db import models

# Create your models here.
class student(models.Model):
	name = models.CharField(max_length=40)
	email = models.CharField(max_length=50)
	workingunder = models.CharField(max_length=40)
	searchingon = models.CharField(max_length=500)
	
	def __str__(self):
		return self.email+"-"+self.workingunder+"-"+self.searchingon
class news(models.Model):
	newstext = models.CommaSeparatedIntegerField(max_length=200)
	
	def __str__(self):
		return self.newstext;