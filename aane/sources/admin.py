from django.contrib import admin
from django.db import models
from django.forms import Textarea, TextInput
from .models import PrimarySource, SourceEntry
from calendar import month_abbr

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
    fields = ['source_type', 'title', 'pub_info', 'description', 
    ('year_start', 'year_end'), 'operson_id']
    #inlines = [SourceEntryInline]
    list_display = ('title', 'id', 'source_type', 'pub_info', 'operson_id', 
        'year_start', 'year_end')
    search_fields = ['title']
    list_filter  = ['source_type'] 
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'60'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':60})},
    }

admin.site.register(PrimarySource, PrimarySourceAdmin)

class SourceEntryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [
            'primary_source', 'date_range',
            'entry_text', 'event', 'transaction_note',
            ('aa_id', 'operson_id'), 'name_note', 
            ]}
        ),
        ('Date Info', {'fields': [
            ('low_year', 'low_month', 'low_day'), 
            ('upr_year', 'upr_month', 'upr_day'),
            'date_status', 'date_note',   
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
    list_display = ('entry_text', 'low_year', 'month_day',
        'date_range', 'page_num', 'aa_id', 'operson_id')
    list_filter  = ['primary_source'] 
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'80'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':80})},
    }

    def month_day(self, obj):
        if (obj.low_month):
            display_date = month_abbr[obj.low_month]
            if (obj.low_day):
                display_date += " - " + str(obj.low_day)
            return display_date
    month_day.short_description = 'Mo. Day'   

admin.site.register(SourceEntry, SourceEntryAdmin)
