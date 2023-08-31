"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.HomeView.as_view(), name='home'),

    url(r'^sources/', include('sources.urls', namespace="sources")),
    url(r'^people/', include('people.urls', namespace="people")),

    url(r'^admin/', include(admin.site.urls)),
]
Switch to 2.2 syntax
"""

from django.contrib import admin
from django.urls import include, path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from .schema import schema
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('team/', views.TeamView.as_view(), name='team_home'),
    path('graphql/', 
       csrf_exempt(GraphQLView.as_view(graphiql=True)), 
       name='graphql'),
    path('sources/', include('sources.urls', namespace="sources")),
    path('people/', include('people.urls', namespace="people")),
    path('about/', include('about.urls', namespace="about")),

    path('admin/', admin.site.urls),
]

