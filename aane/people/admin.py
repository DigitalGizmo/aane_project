from django.contrib import admin
from .models import AAPerson, OPerson


class AAPersonAdmin(admin.ModelAdmin):
    fields = ['name', 'first_name','last_name', 'alt_name_spelling', 'freed_name', 'gender',
            'known_status', 'freed_status',
            'birth_year', 'death_year', 'bio', 'owners', 'place_of_origin', 
            'owner_id','first_appearance_year', 'last_appearance_year', 
            'free_start_year']
    list_display = ('name', 'id', 'owner_id', 'first_name', 'last_name', 'alt_name_spelling', 
        'known_status', 'freed_status', 'free_start_year', 'birth_year', 'death_year')
    search_fields = ['name']
    filter_horizontal = ['owners']
    list_filter  = ['known_status', 'freed_status'] 

admin.site.register(AAPerson, AAPersonAdmin)


class OPersonAdmin(admin.ModelAdmin):
    fields = ['name', 'first_name','last_name', 'title', 'gender', 'role', 'race', 
            'bio', 'birth_year', 'death_year', 'year_lower', 
            'year_upper']
    list_display = ('name', 'id', 'first_name', 'last_name', 'title', 'birth_year', 
            'death_year', 'year_lower')
    search_fields = ['name']

admin.site.register(OPerson, OPersonAdmin)
