from django.shortcuts import render
from django.template import loader
from .models import newsfield,aboutfield
from django.http import HttpResponse
# Create your views here.
def newsdetails(request):
	total_news = newsfield.objects.all()
	template = loader.get_template('homepage/home1.html')
	context = {
	'total_news':total_news,
	}
	return HttpResponse(template.render(context,request))
