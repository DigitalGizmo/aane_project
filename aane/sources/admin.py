from django.contrib import admin
from .models import PrimarySource, SourceEntry
# SourceCollection, 

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
            'entry_text', 'clarified', 'event', 'transaction_note',
            ('aa_id', 'operson_id'), 'name_note', 
            ]}
        ),
        ('Date Info', {'fields': [
            ('low_year', 'low_month', 'low_day'), 
            ('upr_year', 'upr_month', 'upr_day'),
            'date_status', 'date_note',  'date_range', 
        ]}),
        ('Page Info', {'fields': [
            'vol_book', 'page_num',
        ]}),
        ('Monetary Transaction', {'fields': [
            'dollars', 'pounds', 'shillings', 'pence', 'farthing', 
            'notes'], 'classes': ['collapse']
            }),
        ('Legacy Info', {'fields': [
            'legacy_enslaved_id', 'access_order', 'legacy_id', 'pvma_call_num',
        ]}),

    ]
    list_display = ('entry_text', 'low_year', 'low_month', 'low_day',
        'page_num', 'aa_id', 'operson_id')
    list_filter  = ['primary_source'] 
admin.site.register(SourceEntry, SourceEntryAdmin)
