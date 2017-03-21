from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns=[
	url(r'^$',views.index, name = 'index'),
	url(r'^About$',TemplateView.as_view(template_name="fc.html"),

]
