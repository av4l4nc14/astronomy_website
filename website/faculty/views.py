from django.shortcuts import render

from django.template import loader
from .models import Faculty
from django.http import HttpResponse
# Create your views here.


def index(request):
	all_faculty=Faculty.objects.all()
	
	template = loader.get_template('faculty/fc.html')
        if request.POST :
        	all_faculty=Faculty.objects.filter(name__contains=request.POST['search'])     
	context={
	'all_faculty':all_faculty,
	}

	return HttpResponse(template.render(context,request))
	


