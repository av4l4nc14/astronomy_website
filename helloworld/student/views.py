from django.shortcuts import render
from . import views
from django.template import loader
from .models import student,news
from django.http import HttpResponse
# Create your views here.
def index(request):
	all_students = student.objects.all()
	template = loader.get_template('student/indexfile.html')
	context ={
	'all_students':all_students,
	}
	return HttpResponse(template.render(context,request))
	
def newdetails(request):
	total_news = news.objects.all()
	template = loader.get_template('student/newsfile.html')
	context = {
	'total_news':total_news,
	}
	return HttpResponse(template.render(context,request))