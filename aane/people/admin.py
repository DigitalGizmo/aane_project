from typing import Any
from django.contrib import admin
from django.db import models
from django.http.request import HttpRequest
from tinymce.widgets import TinyMCE
from tinymce import models as tinymce_models
from .models import AAPerson, OPerson
from locations.models import Town


class AAPersonAdmin(admin.ModelAdmin):
    fields = ['name', ('first_name','last_name'), 
              ('alt_name_spelling', 'freed_name'), 
              ('gender', 'freed_status', 'free_start_year'),
            ('birth_year', 'is_birth_circa','death_year', 
             'is_death_circa', 'tier'), 
            ('research_status', 'confidence', 'known_status'), 
            'bio_html', 'note', 'owners', 'owner_id',  
            'locations','place_of_origin',
            ('first_appearance_year', 'last_appearance_year'), 
            ]
    readonly_fields = ('owner_id', 'known_status')
    list_display = ('name', 'id', 'first_name', 'last_name', 
                    'alt_name_spelling', 'research_status', 
                    'get_locations', 'freed_status', 
                    'free_start_year', 'birth_year', 'death_year')
    search_fields = ['name']
    filter_horizontal = ['owners', 'locations']
    list_filter  = ['tier', 'research_status', 'freed_status'] 

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(
            first_location=models.Min('locations__title')
        )
    @admin.display(description='Town',ordering='first_location')
    def get_locations(self, obj):
        return ", ".join([str(location) for location in obj.locations.all()])

    # defined in Person model
    # def get_ordering(self, request):
    #     return ['first_location']

admin.site.register(AAPerson, AAPersonAdmin)


class OPersonAdmin(admin.ModelAdmin):
    fields = ['name', 'first_name',('last_name', 'title'), 
              ('gender', 'role', 'race'), 
            ('birth_year', 'death_year'), 
            ('year_lower', 'year_upper'), 'research_status',
            'bio_html', 'note', 'locations']
    list_display = ('name', 'id', 'first_name', 'last_name', 'title', 
                    'research_status', 'get_locations', 'birth_year', 
                    'death_year', 'year_lower')
    filter_horizontal = ['locations']
    search_fields = ['name']
    list_filter  = ['research_status'] 

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(
            first_location=models.Min('locations__title')
        )
    @admin.display(description='Town',ordering='first_location')
    def get_locations(self, obj):
        return ", ".join([str(location) for location in obj.locations.all()])


admin.site.register(OPerson, OPersonAdmin)
