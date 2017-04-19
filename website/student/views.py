from django.shortcuts import render

from django.template import loader
from .models import student
from django.http import HttpResponse
# Create your views here.


def index(request):
	all_student=student.objects.all()
	
	template = loader.get_template('student/student.html')
        if request.POST :
        	all_student=student.objects.filter(name__contains=request.POST['search'])     
	context={
	'all_student':all_student,
	}

	return HttpResponse(template.render(context,request))
	


