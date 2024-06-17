from django.contrib import admin
from .models import AAPerson, OPerson


class AAPersonAdmin(admin.ModelAdmin):
    fields = ['name', 'first_name','last_name', 'alt_name_spelling', 'freed_name', 
            ('gender', 'freed_status'),
            ('research_status', 'known_status'), 
            ('birth_year', 'death_year', 'free_start_year'), 
            'bio', 'owners', 'locations',  
            ('owner_id', 'place_of_origin'),
            ('first_appearance_year', 'last_appearance_year'), 
            ]
    list_display = ('name', 'id', 'owner_id', 'first_name', 'last_name', 
                    'alt_name_spelling', 'research_status', 'freed_status', 
                    'free_start_year', 'birth_year', 'death_year')
    search_fields = ['name']
    filter_horizontal = ['owners', 'locations']
    list_filter  = ['research_status', 'freed_status'] 

admin.site.register(AAPerson, AAPersonAdmin)


class OPersonAdmin(admin.ModelAdmin):
    fields = ['name', 'first_name','last_name', 'title', 
              ('gender', 'role', 'race'), 
            'bio', ('birth_year', 'death_year'), 
            ('year_lower', 'year_upper'), 'research_status',
            'locations']
    list_display = ('name', 'id', 'first_name', 'last_name', 'title', 
                    'research_status', 'birth_year', 'death_year', 'year_lower')
    filter_horizontal = ['locations']
    search_fields = ['name']

admin.site.register(OPerson, OPersonAdmin)
