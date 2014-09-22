from django.conf.urls import patterns, include, url

from polls import views
'''
Created on Sep 22, 2014

@author: eqioouy
'''
from django.http import HttpResponse

urlpatterns= patterns('',url(r'^$',views.index,name='index'))