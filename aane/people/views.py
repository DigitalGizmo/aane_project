from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.db.models import Q
from django.views.generic.edit import FormMixin
from .models import AAPerson, OPerson
from .forms import PersonSearchForm

"""
def aa_index(request):
    research_object_list = AAPerson.objects.all().order_by('name')
    return render(request, 'people/aapeople_index.html', 
            {'research_object_list': research_object_list})
"""

class AAPersonListView(FormMixin, generic.ListView):
    model = AAPerson
    # context_object_name = 'aaperson_list'
    #template_name = 'people/aaperson_index.html'

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
            q = form.cleaned_data['q']
            freed_status_list = form.cleaned_data['freedStatus']

            if q:
                self.object_list = self.object_list.filter(Q(name__icontains=q) )
                #  | Q(narrative__icontains=q)

            if len(freed_status_list) > 0 :
                # per undocumented .add method for Q objects
                # https://bradmontgomery.net/blog/adding-q-objects-in-django/
                # Get initial (0), then add
                qquery = Q(freed_status=freed_status_list[0])

                for freed_choice in freed_status_list[1:]:
                    qquery.add((Q(freed_status=freed_choice )), 'OR' ) 

                self.object_list = self.object_list.filter(qquery)





        # remove any duplicates
        self.object_list = self.object_list.distinct()

        context = self.get_context_data(form=form)
        context['result_count'] = len(self.object_list)
        return self.render_to_response(context)

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

