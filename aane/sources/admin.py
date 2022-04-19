from dataclasses import fields
from django.contrib import admin
from django.db import models
from django.forms import Textarea, TextInput
from .models import PrimarySource, SourceEntry, SourceType, Volume
from calendar import month_abbr

"""
class SourceCollectionAdmin(admin.ModelAdmin):
    fields = ['title']
    list_display = ('title')
admin.site.register(SourceCollection, SourceCollectionAdmin)
"""

class VolumeInline(admin.StackedInline):
    model = Volume
    extra = 2
    fields = ['primary_source', 'title', 
    ('volume_scan_id', 'accession_num', 'other_accession_num'),
    ('year_start', 'year_end', 'note')]
    formfield_overrides = {
        # models.CharField: {'widget': TextInput(attrs={'size':'60'})},
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':80})},
    }

class PrimarySourceAdmin(admin.ModelAdmin): 
    fields = ['title', 'source_classification', 'pub_info', 'description', 
    ('year_start', 'year_end'), 'operson_id']
    list_display = ('title', 'id', 'pub_info', 'operson_id', 
        'year_start', 'year_end')
    search_fields = ['title']
    list_filter  = ['source_classification'] 
    inlines = [VolumeInline]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'60'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':60})},
    }

class SourceTypeAdmin(admin.ModelAdmin):
    fields = [
        'slug', 'title', 'note'
    ]
    list_display = ('slug', 'title')


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

admin.site.register(PrimarySource, PrimarySourceAdmin)
admin.site.register(SourceType, SourceTypeAdmin)
admin.site.register(SourceEntry, SourceEntryAdmin)
