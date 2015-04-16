from django.shortcuts import get_object_or_404, render
from .models import PrimarySource, SourceEntry
from people.models import AAPerson
# new
from django.http import HttpResponseRedirect, HttpResponse # HttpResponse is temporary
from django.core.urlresolvers import reverse
from django.views import generic
from django.core.urlresolvers import reverse_lazy

"""
def index(request):
    research_object_list = PrimarySource.objects.all().order_by('title')
    return render(request, 'sources/index.html', {'research_object_list': research_object_list})
"""

class SourceListView(generic.ListView):
    model = PrimarySource
    context_object_name = 'primarysource_list'
    template_name = 'sources/index.html'

# this displays the Source's Entries as well
class SourceDetailView(generic.DetailView):
    model = PrimarySource
    template_name = 'sources/source_detail.html'

class EntryDetailView(generic.DetailView):
    model = SourceEntry
    template_name = 'sources/entry_detail.html'

class EntryCreateView(generic.CreateView):
    model = SourceEntry
    #fields = ['entry_text']

class EntryUpdateView(generic.UpdateView):
    model = SourceEntry
    # template_name = 'sources/sourceentry_form.html'
    fields = ['entry_text', 'clarified', 'aa_id', 'secondary_person_id', 'name_note']

class EntryDeleteView(generic.DeleteView):
    model = SourceEntry
    success_url = reverse_lazy('author-list')

# probably temp - needed for generic forms tutorial
class EntryListView(generic.ListView):
    model = SourceEntry
    context_object_name = 'sourceentry_list'
    template_name = 'sources/entry_index.html'


