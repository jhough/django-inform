from django.conf.urls import url

from .views import PollsListView, PollsDetailView, PollsResultsView, vote

urlpatterns = [
    url(regex=r'^$', view=PollsListView.as_view(), name='list'),
    url(regex=r'^(?P<pk>\d+)$', view=PollsDetailView.as_view(), name='detail'),
    url(regex=r'^(?P<pk>\d+)/results/$', view=PollsResultsView.as_view(), name='results'),
    url(regex=r'^(?P<poll_id>\d+)/vote/$', view=vote, name='vote'),
]