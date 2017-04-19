from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
from django.contrib.auth.views import login,logout
urlpatterns=[
	url(r'^$',views.index, name = 'index'),
	url(r'^flogin/$',login,name='login'),
	url(r'^flogout/$',logout,{'next_page':'/'}, name='logout'),
        
]
