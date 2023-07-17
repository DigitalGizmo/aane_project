from django.urls import include, path
from django.views.generic import TemplateView
from . import views

app_name = "about"

urlpatterns = [

    # path('project/', views.AAPersonListView.as_view(), name='aaperson_index'),
    path('project/', TemplateView.as_view(template_name="about/project.html"), name='project'),
    path('database/', TemplateView.as_view(template_name="about/database.html"), name='database'),
    path('funders/', TemplateView.as_view(template_name="about/funders.html"), name='funders'),
    path('pvms/', TemplateView.as_view(template_name="about/pvma.html"), name='pvma'),
    path('contact/', TemplateView.as_view(template_name="about/contact.html"), name='contact'),

]
