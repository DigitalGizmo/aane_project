from django.shortcuts import get_object_or_404, render
from .models import AAPerson, OPerson
from django.views import generic

"""
def aa_index(request):
    research_object_list = AAPerson.objects.all().order_by('name')
    return render(request, 'people/aapeople_index.html', 
            {'research_object_list': research_object_list})
"""

class AAPersonListView(generic.ListView):
    model = AAPerson
    # context_object_name = 'aaperson_list'
    #template_name = 'people/aaperson_index.html'

class AAPersonDetailView(generic.DetailView):
    model = AAPerson
    #template_name = 'people/aaperson_detail.html' # default

class AAPersonEntriesDetailView(generic.DetailView):
    model = AAPerson
    template_name = 'people/aaperson_entries.html' 
    # includes list of entries for this peson as defined in AAPerson model.

class AAPersonUpdateView(generic.UpdateView):
    model = AAPerson
    #template_name = 'people/aaperson_form.html' 

class AAPersonCreateView(generic.CreateView):
    model = AAPerson
    template_name = 'people/aaperson_create.html' 

class OPersonListView(generic.ListView):
    model = OPerson
    # context_object_name = 'operson_list'
    #template_name = 'people/operson_index.html'

class OPersonDetailView(generic.DetailView):
    model = OPerson
    #template_name = 'people/operson_detail.html' # default

