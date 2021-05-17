from django.conf.urls import url
from . import views

app_name = "people"

urlpatterns = [

    url(r'^aapersons/$', views.AAPersonListView.as_view(), name='aaperson_index'),
    url(r'^aaperson/(?P<pk>\d+)/$', views.AAPersonDetailView.as_view(), 
    				name='aaperson_detail'),
    url(r'^aaperson/entries/(?P<pk>\d+)/$', views.AAPersonEntriesDetailView.as_view(), 
    				name='aaperson_entries'),
    url(r'^aaperson/update/(?P<pk>\d+)/$', views.AAPersonUpdateView.as_view(), 
    				name='aaperson_update'),
    url(r'^aaperson/add/$', views.AAPersonCreateView.as_view(), name='aaperson_add'),
    url(r'^opersons/$', views.OPersonListView.as_view(), name='operson_index'),
    url(r'^operson/(?P<pk>\d+)/$', views.OPersonDetailView.as_view(), 
    				name='operson_detail'),

]
