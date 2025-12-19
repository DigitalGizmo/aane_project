from multiprocessing import context
# import re
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from rest_framework import viewsets
from django.urls import reverse_lazy, reverse
from django.db.models import F
# from django.views import generic
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from .models import PrimarySource, SourceEntry, Volume
from .forms import SourceSearchForm, EntrySearchForm
# from people.models import AAPerson
from .serializers import SourceEntrySerializer

"""
def index(request):
    research_object_list = PrimarySource.objects.all().order_by('title')
    return render(request, 'sources/index.html', {'research_object_list': research_object_list})
"""

class SourceListView(FormMixin, ListView):
    model = PrimarySource
    context_object_name = 'primarysource_list'
    template_name = 'sources/index.html'
    # For search and filter
    paginate_by=32
    form_class = SourceSearchForm

    def get_form_kwargs(self):
        return {
            'initial': self.get_initial(), # won't be using this
            'prefix': self.get_prefix(),  # don't know what this is
            'data': self.request.GET # or self.init_data # None  # will add my data here
        }

    def get(self, request,*args, **kwargs):
        self.object_list = self.get_queryset()
        form = self.get_form(self.get_form_class())

        if form.is_valid():
            q = form.cleaned_data['q']
            type_list = form.cleaned_data['sourceTypes']

            if q:
                self.object_list = self.object_list.filter(Q(title__icontains=q) )
                #  | Q(narrative__icontains=q)
            if len(type_list) > 0 :
                # per undocumented .add method for Q objects
                # https://bradmontgomery.net/blog/adding-q-objects-in-django/
                # Get initial (0), then add
                qquery = Q(source_type__slug=type_list[0])

                for type_choice in type_list[1:]:
                    qquery.add((Q(source_type__slug=type_choice)), 'OR' ) 

                self.object_list = self.object_list.filter(qquery)

        # remove any duplicates
        self.object_list = self.object_list.distinct()

        context = self.get_context_data(form=form)
        context['result_count'] = len(self.object_list)
        return self.render_to_response(context)

"""""
Mistakenly started - really wanted entries per volume.
But this may come in handy later
"""""
# class VolumeListView(generic.ListView):
#     model = PrimarySource
#     context_object_name = 'volume_list'
#     template_name = 'sources/volume_index.html'

# this displays the Source's Entries as well
class SourceDetailView(DetailView):
    model = PrimarySource
    template_name = 'sources/source_detail.html'

    # # Get list of entries with no volume assignment
    # def get_context_data(self, **kwargs):
    #     # Get the context
    #     context = super(SourceDetailView, self).get_context_data(**kwargs)
    #     # Get this source object
    #     source_object = super(SourceDetailView, self).get_object()
    #     # Filter for entries where volume_id === null
    #     # entries_no_vol = source_object.sourceentry_set.all
    #     entries_no_vol = source_object.sourceentry_set.filter(volume_id__isnull=True)

    #     # Add updated variable to context
    #     context.update({
    #         'entries_no_vol': entries_no_vol,
    #         })
    #     return context    
        


# New July 2022 - per volume detail
class VolumeDetailView(DetailView):
    model = Volume
    template_name = 'sources/volume_detail.html'

class EntryDetailView(DetailView):
    model = SourceEntry 
    # template_name = 'sources/entry_detail.html'
    template_name = 'sources/entry_pop_detail.html'
    # get the entry record
    def get_context_data(self, **kwargs):
        # Get the context
        context = super(EntryDetailView, self).get_context_data(**kwargs)
        # Get this entry object
        entry_object = super(EntryDetailView, self).get_object()

        entry_ids = [30,41,45,50]
        # initial_index = 2
        initial_index = entry_ids[2]
        print('index: ' + str(initial_index))
        # # Get the percentage from top
        # view_percent_top = 0
        # if entry_object.percent_top:
        #     view_percent_top = entry_object.percent_top
        # view_percent_height = 8
        # if entry_object.percent_left:
        #     view_percent_left = entry_object.percent_left
        # view_percent_width = 100
        # if entry_object.percent_height:
        #     view_percent_height = entry_object.percent_height
        # view_percent_left = 0
        # if entry_object.percent_right:
        #     view_percent_width = entry_object.percent_right
        # Add updated variable to context
        context.update({
            'entry_ids': entry_ids,
            'initial_index': initial_index
            # 'view_percent_top': view_percent_top,
            # 'view_percent_left': view_percent_left,
            # 'view_percent_width': view_percent_width,
            # 'view_percent_height': view_percent_height,

            })
        return context    

# For search all entries page
class EntryListView(FormMixin, ListView): # FormMixin,
    """Shows all entries
    """ 
    model = SourceEntry
    context_object_name = 'sourceentry_list'
    # template_name = 'sources/entries_all.html'
    # For search and filter
    paginate_by=32
    form_class = EntrySearchForm

    def get_form_kwargs(self):
        return {
            'initial': self.get_initial(), # won't be using this
            'prefix': self.get_prefix(),  # don't know what this is
            'data': self.request.GET # or self.init_data # None  # will add my data here
        }

    def get(self, request,*args, **kwargs):
        self.object_list = self.get_queryset()
        form = self.get_form(self.get_form_class())

        if form.is_valid():
            q = form.cleaned_data['q']
            year = form.cleaned_data['year']
            # type_list = form.cleaned_data['sourceTypes']
            noAaId = form.cleaned_data['noAaId']
            sortOrder = form.cleaned_data['sortOrder']
            print("got to form valid")

            if q:
                print("got to if q")
                self.object_list = self.object_list.filter(Q(entry_text__icontains=q) )
                #  | Q(narrative__icontains=q)

            if year:
                print("got to if year")

                self.object_list = self.object_list.filter(Q(low_year__icontains=year) )
                #  | Q(narrative__icontains=q)

            # Optional sort
            if sortOrder:
                if(sortOrder == 'monetary'):
                    self.object_list = self.object_list.order_by(F('dollars').desc(nulls_last=True), F('pounds').desc(nulls_last=True), F('shillings').desc(nulls_last=True), F('pence').desc(nulls_last=True))
                else:
                    self.object_list = self.object_list.order_by(sortOrder)

            if len(noAaId) > 0 :
                # self.object_list = self.object_list.filter(Q(aa_id__isnull=True) )
                self.object_list = self.object_list.filter(Q(aa_persons__isnull=True))

        # remove any duplicates
        self.object_list = self.object_list.distinct()

        context = self.get_context_data(form=form)
        context['result_count'] = len(self.object_list)
        return self.render_to_response(context)


class SourceEntryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SourceEntry.objects.filter(id__lte=200).order_by('id')
    serializer_class = SourceEntrySerializer
    lookup_field = 'entry_text_html'

# class EntryCreateView(generic.CreateView):
#     model = SourceEntry
#     #fields = ['entry_ text']

# class EntryUpdateView(generic.UpdateView):
#     model = SourceEntry
#     # template_name = 'sources/sourceentry_form.html'
#     fields = ['entry_ text', 'clarified', 'aa_id', 'secondary_person_id', 'name_note']

# class EntryDeleteView(generic.DeleteView):
#     model = SourceEntry
#     success_url = reverse_lazy('author-list')

# # probably temp - needed for generic forms tutorial
# class EntryListView(generic.ListView):
#     model = SourceEntry
#     context_object_name = 'sourceentry_list'
#     template_name = 'sources/entry_index.html'


