#from django.conf.urls import patterns, url
from .views import PollsListView, PollsDetailView, PollsResultsView, vote

#from __future__ import absolute_import, unicode_literals
from django.conf.urls import url
#from . import views

#urlpatterns = patterns('',
#    url(r'^$', IndexView.as_view(), name='index'),
#    url(r'^(?P<pk>\d+)/$', DetailView.as_view(), name='detail'),
#    url(r'^(?P<pk>\d+)/results/$', ResultsView.as_view(), name='results'),
#    url(r'^(?P<poll_id>\d+)/vote/$', vote, name='vote'),
#)

urlpatterns = [
    url(regex=r'^$', view=PollsListView.as_view(), name='list'),
    url(regex=r'^(?P<pk>\d+)$', view=PollsDetailView.as_view(), name='detail'),
    url(regex=r'^(?P<pk>\d+)/results/$', view=PollsResultsView.as_view(), name='results'),
    url(regex=r'^(?P<poll_id>\d+)/vote/$', view=vote, name='vote'),
]