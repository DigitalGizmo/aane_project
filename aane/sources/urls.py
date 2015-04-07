from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('sources.views',
    # Examples:
    # url(r'^$', 'aane.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.SourceListView.as_view(), name='index'),
    url(r'^source/(?P<pk>\d+)/$', views.SourceDetailView.as_view(), name='source_detail'),
    # editing
    url(r'entry/add/$', views.EntryCreateView.as_view(), name='entry_add'),
    url(r'entry/update/(?P<pk>\d+)/$', views.EntryUpdateView.as_view(), name='entry_update'),
    url(r'entry/(?P<pk>\d+)/delete/$', views.EntryDeleteView.as_view(), name='entry_delete'),

    #temp
    url(r'^entry/(?P<pk>\d+)/$', views.EntryDetailView.as_view(), name='entry_detail'),
    url(r'^entries/$', views.EntryListView.as_view(), name='all_entries'),
)
