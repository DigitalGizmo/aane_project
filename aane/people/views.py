from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.db.models import Q, Count
from rest_framework import viewsets
from django.views.generic.edit import FormMixin
from .models import AAPerson, OPerson
from .forms import PersonSearchForm
from .serializers import AAPersonSerializer, OPersonSerializer

"""
def aa_index(request):
    research_object_list = AAPerson.objects.all().order_by('name')
    return render(request, 'people/aapeople_index.html', 
            {'research_object_list': research_object_list})
"""

class AAPersonListView(FormMixin, generic.ListView):
    model = AAPerson
    # context_object_name = 'aaperson_list'
    #template_name = 'people/aaperson_list.html'

    # For search and filter
    paginate_by=40
    form_class = PersonSearchForm

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
            tier_value = form.cleaned_data['tier']
            for_name = form.cleaned_data['for_name']
            in_bio = form.cleaned_data['in_bio']
            freed_status_list = form.cleaned_data['freedStatus']
            sortOrder = form.cleaned_data['sortOrder']

            # Remove inactive entries
            self.object_list = self.object_list.filter(Q(research_status__gt=1) )

            # Select Tier
            if tier_value is None:
                self.object_list = self.object_list.filter(Q(tier=1) )
            else: 
                self.object_list = self.object_list.filter(Q(tier=tier_value) )

            if for_name:
                print('for_name: ' + for_name)
                self.object_list = self.object_list.filter(Q(name__icontains=for_name) )
                #  | Q(narrative__icontains=q)

            if in_bio:
                self.object_list = self.object_list.filter(Q(bio__icontains=in_bio) )

            if len(freed_status_list) > 0 :
                # per undocumented .add method for Q objects
                # https://bradmontgomery.net/blog/adding-q-objects-in-django/
                # Get initial (0), then add
                qquery = Q(freed_status=freed_status_list[0])

                for freed_choice in freed_status_list[1:]:
                    qquery.add((Q(freed_status=freed_choice )), 'OR' ) 

                self.object_list = self.object_list.filter(qquery)
            
            # Optional sort
            if sortOrder:
                self.object_list = self.object_list.order_by(sortOrder)
                # self.object_list = self.object_list.order_by(sortOrder_list[0])
                #  | Q(narrative__icontains=q)


        # remove any duplicates
        self.object_list = self.object_list.distinct()

        context = self.get_context_data(form=form)
        context['result_count'] = len(self.object_list)
        return self.render_to_response(context)


class AAPersonOtherListView(FormMixin, generic.ListView):
    model = AAPerson
    # context_object_name = 'aaperson_list'
    template_name = 'people/aaperson_other.html'

    # For search and filter
    paginate_by=40
    form_class = PersonSearchForm

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
            # tier_value = form.cleaned_data['tier']
            for_name = form.cleaned_data['for_name']
            in_bio = form.cleaned_data['in_bio']
            freed_status_list = form.cleaned_data['freedStatus']
            sortOrder = form.cleaned_data['sortOrder']

            # Remove inactive entries
            self.object_list = self.object_list.filter(Q(research_status__gt=1) )

            # Select Tier
            self.object_list = self.object_list.filter(Q(tier=0) )

            if for_name:
                print('for_name: ' + for_name)
                self.object_list = self.object_list.filter(Q(name__icontains=for_name) )
                #  | Q(narrative__icontains=q)

            if in_bio:
                self.object_list = self.object_list.filter(Q(bio__icontains=in_bio) )

            if len(freed_status_list) > 0 :
                # per undocumented .add method for Q objects
                # https://bradmontgomery.net/blog/adding-q-objects-in-django/
                # Get initial (0), then add
                qquery = Q(freed_status=freed_status_list[0])

                for freed_choice in freed_status_list[1:]:
                    qquery.add((Q(freed_status=freed_choice )), 'OR' ) 

                self.object_list = self.object_list.filter(qquery)
            
            # Optional sort
            if sortOrder:
                self.object_list = self.object_list.order_by(sortOrder)
                # self.object_list = self.object_list.order_by(sortOrder_list[0])
                #  | Q(narrative__icontains=q)


        # remove any duplicates
        self.object_list = self.object_list.distinct()

        context = self.get_context_data(form=form)
        context['result_count'] = len(self.object_list)
        return self.render_to_response(context)


class AAPersonZeroListView(FormMixin, generic.ListView):
    """Team page to research zero entries
    """
    model = AAPerson
    # context_object_name = 'aaperson_list'
    template_name = 'people/aaperson_team.html'

    # For search and filter
    paginate_by=40
    form_class = PersonSearchForm

    def get_form_kwargs(self):
        return {
            'initial': self.get_initial(), # won't be using this
            'prefix': self.get_prefix(),  # don't know what this is
            'data': self.request.GET # or self.init_data # None  # will add my data here
        }

    def get(self, request,*args, **kwargs):


        # self.object_list = self.get_queryset()
        # Courtesy of Claue 3.5
        self.object_list = self.model.objects.annotate(
            source_count=Count('aa_persons')
        )
        form = self.get_form(self.get_form_class())

        # self.object_list = self.object_list.filter(Q(source_count=0))

        if form.is_valid():
            for_name= form.cleaned_data['for_name']
            freed_status_list = form.cleaned_data['freedStatus']
            research_values = form.cleaned_data['researchLevel']
            sortOrder = form.cleaned_data['sortOrder']
            has_source_entries = form.cleaned_data['hasSourceEntries']
            tier_value = form.cleaned_data['tierLevel']


            # has entries or not
            if has_source_entries:
                print(' has source entries value: ' + str(has_source_entries))
                if int(has_source_entries[0]) == 0:
                    self.object_list = self.object_list.filter(Q(source_count=0) )
                else:
                    self.object_list = self.object_list.filter(Q(source_count__gt=0) )

            # has entries or not
            # if has_source_entries:
            # print(' has source entries value: ' + str(has_source_entries))
            # if has_source_entries == 1:
            #     self.object_list = self.object_list.filter(Q(source_count=0) )
            # elif has_source_entries == 2:
            #     self.object_list = self.object_list.filter(Q(source_count__gt=0) )

            # Tier
            if tier_value:
                print(' tier value: ' + str(tier_value))
                if int(tier_value[0]) == 0:
                    self.object_list = self.object_list.filter(Q(tier=0) )
                else:
                    self.object_list = self.object_list.filter(Q(tier=1) )

            if for_name:
                self.object_list = self.object_list.filter(Q(name__icontains=for_name) )
                #  | Q(narrative__icontains=q)

            if len(freed_status_list) > 0 :
                # per undocumented .add method for Q objects
                # https://bradmontgomery.net/blog/adding-q-objects-in-django/
                # Get initial (0), then add
                qquery = Q(freed_status=freed_status_list[0])

                for freed_choice in freed_status_list[1:]:
                    qquery.add((Q(freed_status=freed_choice )), 'OR' ) 

                self.object_list = self.object_list.filter(qquery)

            if len(research_values) > 0 :
                # per undocumented .add method for Q objects
                # https://bradmontgomery.net/blog/adding-q-objects-in-django/
                # Get initial (0), then add
                print(' - research_values[0]: ' + str(research_values[0]))
                qquery = Q(research_status=research_values[0])

                for research_choice in research_values[1:]:
                    print(' - research_values[1]: ' + str(research_values[1]))
                    qquery.add((Q(research_status=research_choice )), 'OR' ) 

                self.object_list = self.object_list.filter(qquery)

            # Optional sort
            if sortOrder:
                self.object_list = self.object_list.order_by(sortOrder)
                # self.object_list = self.object_list.order_by(sortOrder_list[0])
                #  | Q(narrative__icontains=q)


        # remove any duplicates
        self.object_list = self.object_list.distinct()

        context = self.get_context_data(form=form)
        context['result_count'] = len(self.object_list)
        return self.render_to_response(context)


class AAPersonDetailView(generic.DetailView):
    model = AAPerson
    #template_name = 'people/aaperson_detail.html' # default

class AAPersonViewSet(viewsets.ReadOnlyModelViewSet):
    # queryset = AAPerson.objects.filter(bio='{"delta":"","html":""}').order_by('id')
    queryset = AAPerson.objects.filter(~Q(bio='{"delta":"","html":""}')).order_by('id')
    # queryset = AAPerson.objects.all().order_by('id')
    # queryset.add(~Q(bio=''), 'AND' )
    # queryset = AAPerson.objects.all().order_by('id')
    serializer_class = AAPersonSerializer
    lookup_field = 'name'

class OPersonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OPerson.objects.filter(~Q(bio='{"delta":"","html":""}')).order_by('id')
    serializer_class = OPersonSerializer
    lookup_field = 'name'

class OPersonListView(generic.ListView):
    model = OPerson
    # context_object_name = 'operson_list'
    #template_name = 'people/operson_index.html'

class OPersonDetailView(generic.DetailView):
    model = OPerson
    #template_name = 'people/operson_detail.html' # default

