from django.contrib import admin
from django.db import models
from django.forms import Textarea, TextInput
from .models import PrimarySource, SourceEntry

"""
class SourceCollectionAdmin(admin.ModelAdmin):
    fields = ['title']
    list_display = ('title')
admin.site.register(SourceCollection, SourceCollectionAdmin)
"""

class SourceEntryInline(admin.StackedInline):
    model = SourceEntry
    extra = 3

class PrimarySourceAdmin(admin.ModelAdmin):
    fields = ['source_type', 'title', 'pub_info', 'description', 'year_start', 
    'year_end', 'operson_id']
    #inlines = [SourceEntryInline]
    list_display = ('title', 'id', 'source_type', 'pub_info', 'operson_id', 
        'year_start', 'year_end')
    search_fields = ['title']
    list_filter  = ['source_type'] 
admin.site.register(PrimarySource, PrimarySourceAdmin)

class SourceEntryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [
            'primary_source', 
            'entry_text', 'event', 'transaction_note',
            ('aa_id', 'operson_id'), 'name_note', 
            ]}
        ),
        ('Date Info', {'fields': [
            ('low_year', 'low_month', 'low_day'), 
            ('upr_year', 'upr_month', 'upr_day'),
            ('date_range','date_status'), 'date_note',   
        ]}),
        ('Image Info', {'fields': [
            'image_name', 'image_source', 'other_image_source',
            'scan_date',
            ('vol_book', 'page_num'),
            'scan_note',], 'classes': ['collapse']
        }),
        ('Monetary Transaction', {'fields': [
            'dollars', 'pounds', 'shillings', 'pence', 'farthing', 
            'notes'], 'classes': ['collapse']
        }),
        ('Legacy Info', {'fields': [
            'legacy_enslaved_id', 'access_order', 'legacy_id', 'pvma_call_num',
            ], 'classes': ['collapse']
        }),
        ('Obsolete info', {'fields': [
                'clarified',  ], 'classes': ['collapse']
        }),
    ]
    list_display = ('entry_text', 'low_year', 'low_month', 'low_day',
        'page_num', 'aa_id', 'operson_id')
    list_filter  = ['primary_source'] 
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'80'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':80})},
    }

admin.site.register(SourceEntry, SourceEntryAdmin)
