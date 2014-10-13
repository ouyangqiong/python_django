from django.conf.urls import patterns, include, url

from polls import views
'''
Created on Sep 22, 2014

@author: eqioouy
'''
from django.http import HttpResponse

urlpatterns= patterns('',
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^(?P<pk>\d+)/$',views.DetailView.as_view(),name="detail"),
    url(r'^(?P<question_id>\d+)/vote/$',views.vote,name="vote"),
    url(r'^(?P<pk>\d+)/results/$',views.ResultsView.as_view(),name="results"),
)
