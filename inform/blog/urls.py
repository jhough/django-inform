from __future__ import absolute_import, unicode_literals
from django.conf.urls import url
from .views import PostListView, PostDetailView


urlpatterns = [
    url(regex=r'^$', view=PostListView.as_view(), name='list'),
    url(regex=r'^(?P<pk>\d+)$', view=PostDetailView.as_view(), name='detail'),
]