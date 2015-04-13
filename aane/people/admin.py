from django.contrib import admin
from .models import AAPerson, OPerson


class AAPersonAdmin(admin.ModelAdmin):
    fields = ['name', 'first_name','last_name','gender', 'birth_year', 'death_year', 
            'bio', 'owners', 'place_of_origin', 'owner_id','first_appearance_year',
            'last_appearance_year', 'free_start_year']
    list_display = ('name', 'id', 'first_name', 'last_name', 'birth_year', 
        'death_year', 'owner_id', 'place_of_origin')
    search_fields = ['name']
    filter_horizontal = ['owners']

admin.site.register(AAPerson, AAPersonAdmin)


class OPersonAdmin(admin.ModelAdmin):
    fields = ['name', 'first_name','last_name', 'title', 'gender', 'role', 'race', 
            'bio', 'birth_year', 'death_year', 'year_lower', 
            'year_upper']
    list_display = ('name', 'id', 'first_name', 'last_name', 'title', 'birth_year', 'death_year', 'year_lower')
    search_fields = ['name']

admin.site.register(OPerson, OPersonAdmin)
