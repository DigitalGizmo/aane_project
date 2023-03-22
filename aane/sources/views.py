from multiprocessing import context
import re
from django.shortcuts import get_object_or_404, render
from .models import PrimarySource, SourceEntry, Volume
from people.models import AAPerson
# new
from django.http import HttpResponseRedirect, HttpResponse # HttpResponse is temporary
from django.urls import reverse_lazy, reverse
from django.views import generic

"""
def index(request):
    research_object_list = PrimarySource.objects.all().order_by('title')
    return render(request, 'sources/index.html', {'research_object_list': research_object_list})
"""

class SourceListView(generic.ListView):
    model = PrimarySource
    context_object_name = 'primarysource_list'
    template_name = 'sources/index.html'

"""""
Mistakenly started - really wanted entries per volume.
But this may come in handy later
"""""
# class VolumeListView(generic.ListView):
#     model = PrimarySource
#     context_object_name = 'volume_list'
#     template_name = 'sources/volume_index.html'

# this displays the Source's Entries as well
class SourceDetailView(generic.DetailView):
    model = PrimarySource
    template_name = 'sources/source_detail.html'

    # Get list of entries with no volume assignment
    def get_context_data(self, **kwargs):
        # Get the context
        context = super(SourceDetailView, self).get_context_data(**kwargs)
        # Get this source object
        source_object = super(SourceDetailView, self).get_object()
        # Filter for entries where volume_id === null
        # entries_no_vol = source_object.sourceentry_set.all
        entries_no_vol = source_object.sourceentry_set.filter(volume_id__isnull=True)

        # Add updated variable to context
        context.update({
            'entries_no_vol': entries_no_vol,
            })
        return context    
        


# New July 2022 - per volume detail
class VolumeDetailView(generic.DetailView):
    model = Volume
    template_name = 'sources/volume_detail.html'

class EntryDetailView(generic.DetailView):
    model = SourceEntry 
    template_name = 'sources/entry_detail.html'
    # get the entry record
    def get_context_data(self, **kwargs):
        # Get the context
        context = super(EntryDetailView, self).get_context_data(**kwargs)
        # Get this entry object
        entry_object = super(EntryDetailView, self).get_object()
        # Get the percentage from top
        view_percent_top = 0
        if entry_object.percent_top:
            view_percent_top = entry_object.percent_top
        view_percent_height = 8
        if entry_object.percent_left:
            view_percent_left = entry_object.percent_left
        view_percent_width = 100
        if entry_object.percent_height:
            view_percent_height = entry_object.percent_height
        view_percent_left = 0
        if entry_object.percent_right:
            view_percent_width = entry_object.percent_right
        # Add updated variable to context
        context.update({
            'view_percent_top': view_percent_top,
            'view_percent_left': view_percent_left,
            'view_percent_width': view_percent_width,
            'view_percent_height': view_percent_height,
            })
        return context    
        
# class EntryCreateView(generic.CreateView):
#     model = SourceEntry
#     #fields = ['entry_text']

# class EntryUpdateView(generic.UpdateView):
#     model = SourceEntry
#     # template_name = 'sources/sourceentry_form.html'
#     fields = ['entry_text', 'clarified', 'aa_id', 'secondary_person_id', 'name_note']

# class EntryDeleteView(generic.DeleteView):
#     model = SourceEntry
#     success_url = reverse_lazy('author-list')

# # probably temp - needed for generic forms tutorial
# class EntryListView(generic.ListView):
#     model = SourceEntry
#     context_object_name = 'sourceentry_list'
#     template_name = 'sources/entry_index.html'


