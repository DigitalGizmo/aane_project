from django.urls import include, path
from . import views

app_name = "sources"

urlpatterns = [

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
]
