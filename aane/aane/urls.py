from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.HomeView.as_view(), name='home'),

    url(r'^sources/', include('sources.urls', namespace="sources")),
    url(r'^people/', include('people.urls', namespace="people")),

    url(r'^admin/', include(admin.site.urls)),
)
