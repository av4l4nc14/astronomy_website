from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
#from utils.models import UrlMixin
#from utils.models import CreationModificationMixin
# Create your models here.

class Faculty(models.Model):
	name=models.CharField(max_length=50)
	email=models.EmailField(max_length=100)
	institute=models.CharField(max_length=100)
	interests=models.CharField(max_length=200)
	description=models.TextField(max_length=250, blank=True)
	lnk=models.URLField()
	profilepic = models.FileField()
	
	def __str__(self):
		return self.name +" "+ self.email+" "+ self.Institute+" "+self.lnk


class Login_Faculty(models.Model):
	name=models.CharField(max_length=50)
	usrname=models.CharField(max_length=50, primary_key=True)
	passcode=models.CharField(max_length=50)	

