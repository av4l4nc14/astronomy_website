from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from utils.models import UrlMixin
from utils.models import CreationModificationMixin
# Create your models here.

class Faculty(UrlMixin, models.Model):
	name=models.CharField(max_length=50)
	email=models.CharField(max_length=50)
	Institute=models.CharField(max_length=100)
	Interests=models.CharField(max_length=200)
	Description=models.CharField(max_length=250)
	
	def __str__(self):
	return self.name +" "+ self.email+" "+ self.Institute

