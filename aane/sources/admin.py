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

class VolumeAdmin(admin.ModelAdmin):
    fields = ['primary_source', 'title', 
    ('volume_scan_id', 'accession_num', 'other_accession_num'),
    ('year_start', 'year_end', 'note')]
    list_display = ('title', 'id', 'short_source', 'volume_scan_id',
        'accession_num', 'other_accession_num')
    list_filter  = ['primary_source'] 
    search_fields = ['entry_text']
    def short_source(self, obj):
        return obj.primary_source.title[0:20]    
    short_source.short_description = 'Source (truncated)'


class PrimarySourceAdmin(admin.ModelAdmin): 
    fields = ['title', ('source_classification', 'source_type'),
    'pub_info', 'location', 'description', 
    ('year_start', 'year_end'), ('operson_id', 'tiff_location')]
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
            'volume','primary_source', 
            'entry_text', ('event', 'transaction_note'),
            ('aa_id', 'operson_id'), 
            ('name_note', 'data_status'), 'notes',
            ]}
        ),
        ('Image Info', {'fields': [
            'image_name', 'scan_name', # 'image_source', 'other_image_source',
            ('image_status', 'scan_date'),
            ('vol_book', 'page_num'),
            'scan_note',
            ] #, 'classes': ['collapse']
        }),
        ('Entry Highlight', {'fields': [
            ('percent_top', 'percent_height'), 
            ('percent_left', 'percent_right'), 
            ], 'classes': ['collapse']
        }),
        ('Date Info', {'fields': [
            ('low_year', 'low_month', 'low_day'), 
            ('upr_year', 'upr_month', 'upr_day'),
            ('date_status', 'date_range'), 'date_note',  
            ], 'classes': ['collapse']
        }),
        ('Monetary Transaction', {'fields': [
            'dollars', 'pounds', 'shillings', 'pence', 'farthing'
            ], 'classes': ['collapse']
        }),
        ('Legacy Info', {'fields': [
            'legacy_enslaved_id', 'access_order', 'legacy_id', 'pvma_call_num',
            ], 'classes': ['collapse']
        }),
        ('Obsolete info', {'fields': [
                'clarified',  ], 'classes': ['collapse']
        }),
    ]
    list_display = ('entry_text', 'legacy_id', 'low_year', 'month_day',
        'image_name', 'page_num', 'aa_id', 'operson_id', 'data_status',
        'image_status',)
    list_filter  = ['image_status', 'volume'] # , 'primary_source' 
    search_fields = ['entry_text']
    formfield_overrides = {
        # models.CharField: {'widget': TextInput(attrs={'size':'80'})},
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
admin.site.register(Volume, VolumeAdmin)
admin.site.register(SourceType, SourceTypeAdmin)
admin.site.register(SourceEntry, SourceEntryAdmin)
