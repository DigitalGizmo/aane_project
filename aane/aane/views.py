from django.views import generic

# move to general app later
class HomeView(generic.TemplateView):
	template_name = "index.html"