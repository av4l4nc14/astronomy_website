from django.shortcuts import render
from . import views
from django.template import loader
from .models import student,news
from django.http import HttpResponse
# Create your views here.


def index(request):
	all_faculty=Faculty.objects.all()
	
	template = loader.get_template('faculty/index.html')
	context={
	'all_faculty':all_faculty,
	}
	return HttpResponse(template.render(context,request))
	


