from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
#from utils.models import UrlMixin
#from utils.models import CreationModificationMixin
from datetime import datetime, timedelta
# Create your models here.


class newsfield(models.Model):
	description=models.TextField(max_length=250, blank=True)
	date_of_addition=models.DateTimeField(default=datetime.now())
	
	def __str__(self):
		return self.description +" This news was added on "+ self.date_of_addition



class aboutfield(models.Model):
	description=models.TextField(max_length=250,blank=False)
