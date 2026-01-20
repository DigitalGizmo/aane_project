from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import routers
from . import views

app_name = "sources"

router = routers.DefaultRouter()
router.register(r'api', views.SourceEntryViewSet) # views.AAPersonViewSet, 

urlpatterns = [
    path('', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.SourceListView.as_view(), name='index'),
    path('source/<int:pk>/', views.SourceDetailView.as_view(), name='source_detail'),
    path('volume/<int:pk>/', views.VolumeDetailView.as_view(), name='volume_detail'),
    # editing
    # path(r'entry/add/', views.EntryCreateView.as_view(), name='entry_add'),
    # path(r'entry/update/<int:pk>/', views.EntryUpdateView.as_view(), name='entry_update'),
    # path(r'entry/<int:pk>/delete/', views.EntryDeleteView.as_view(), name='entry_delete'),

    path('entry/<int:pk>/', views.EntryDetailView.as_view(), name='entry_detail'),
    path('entries/', 
         views.EntryListView.as_view(template_name="sources/entries_all.html"), name='all_entries'),
    path('team/entries/', 
         views.EntryListView.as_view(template_name="sources/entries_team.html"), name='team_entries'),
    path('test-map/', TemplateView.as_view(template_name='sources/test_map.html'), name='about'),
    path('test-prutt/', TemplateView.as_view(template_name='sources/test_prutt.html'), name='about'),
]

urlpatterns += router.urls