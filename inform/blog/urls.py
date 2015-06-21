from __future__ import absolute_import, unicode_literals
from django.conf.urls import url
from . import views


urlpatterns = [
    url(regex=r'^$', view=views.PostListView.as_view(), name='list'),
    url(regex=r'^(?P<pk>\d+)$', view=views.PostDetailView.as_view(), name='detail'),
]