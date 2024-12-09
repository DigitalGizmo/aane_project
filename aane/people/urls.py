from django.urls import include, path
from rest_framework import routers
from . import views

app_name = "people"

router = routers.DefaultRouter()
router.register(r'api', views.AAPersonViewSet)

urlpatterns = [

    path('', include('rest_framework.urls', namespace='rest_framework')),
    path('aapersons/', views.AAPersonListView.as_view(), name='aaperson_index'),
    path('other-aapersons/', views.AAPersonOtherListView.as_view(), name='aaperson_other'),
    path('aaperson/<int:pk>/', views.AAPersonDetailView.as_view(), 
                  name='aaperson_detail'),
    path('opersons/', views.OPersonListView.as_view(), name='operson_index'),
    path('operson/<int:pk>/', views.OPersonDetailView.as_view(), 
    				name='operson_detail'),
    path('team/zero', views.AAPersonZeroListView.as_view(), name='aaperson_zero'),
]

urlpatterns += router.urls