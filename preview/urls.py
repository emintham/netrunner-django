from django.conf.urls import patterns, url
from preview import views

urlpatterns = patterns('',
	url(r'^$', views.all, name='all'),
	url(r'^index', views.index, name='index'),
)