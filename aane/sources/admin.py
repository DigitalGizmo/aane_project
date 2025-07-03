from dataclasses import fields
from django.contrib import admin
from django.db import models
from django.forms import Textarea, TextInput
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django import forms
from tinymce.widgets import TinyMCE
from tinymce import models as tinymce_models
from .models import PrimarySource, SourceEntry, SourceType, Volume, SourceEntryEditHistory
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
    fields = ['primary_source', 'title', 'legacy_title',
    ('volume_scan_id', 'accession_num', 'other_accession_num'),
    ('year_start', 'month_start', 'day_start'),
    ('year_end', 'month_end', 'day_end'), 'note'
    ]
    list_display = ('id', 'year_start', 'year_end', 'title', 'short_source', 'volume_scan_id',
        'accession_num', 'other_accession_num')
    list_filter  = ['primary_source'] 
    search_fields = ['entry_text_html']
    def short_source(self, obj):
        return obj.primary_source.title[0:20]    
    short_source.short_description = 'Source (truncated)'


class PrimarySourceAdmin(admin.ModelAdmin): 
    fields = ['title', ('source_classification', 'source_type'),
    'pub_info', 'location', 'description', 
    ('year_start', 'year_end'), ('operson_id', 'tiff_location')]
    list_display = ('title', 'id', 'source_type', 'pub_info', # , 'location'
        'operson_id', 'year_start', 'year_end')
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

class SourceEntryEditHistoryInline(admin.StackedInline):
    model = SourceEntryEditHistory
    extra = 1
    fields = [('editor', 'date_edited'), 'note'] # 'active_users',
    readonly_fields = ('date_edited',)

    # def active_users(self, obj):
    #     return obj.editor

class SourceEntryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [
            'volume','primary_source', 
            'entry_text_html', 'interpretive_note', # 'entry_text', 
            'event',
            ('aa_id', 'transaction_note'),
            'aa_persons', 
            ('operson_fk', 'operson_id'),
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
        ('Date Info', {'fields': [
            ('low_year', 'low_month', 'low_day'), 
            ('upr_year', 'upr_month', 'upr_day'),
            ('date_status', 'date_range'), 'date_note',  
            ]
            # , 'classes': ['collapse']
        }),
        ('Monetary Transaction', {'fields': [
            'dollars', 'pounds', 'shillings', 'pence', 'farthing'
            ]
        }),
        ('Legacy Info', {'fields': [
            'legacy_enslaved_id', 'access_order', 'legacy_id', 'pvma_call_num',
            ], 'classes': ['collapse']
        }),
        ('Obsolete info', {'fields': [
                'clarified',  ], 'classes': ['collapse']
        }),

        # ('Entry Highlight', {'fields': [
        #     ('percent_top', 'percent_height'), 
        #     ('percent_left', 'percent_right'), 
        #     ], 'classes': ['collapse']
        # }),
    ]
    readonly_fields = ('aa_id', 'operson_id', 'transaction_note')
    list_display = ('get_entry_text_html', 'id', 'vol_title', 'short_pvma',
        'low_year', 'month_day', 'aa_names', 'operson_fk', 'page_num', 'image_name', 
        'scan_date', 'data_status', 'image_status',) 
    #  'aa_id', 'operson_id', 'operson_fk'
    list_filter  = ['image_status', 'data_status', 'primary_source', 'volume']  
    search_fields = ['entry_text_html', 'image_name']
    filter_horizontal = ['aa_persons']
    formfield_overrides = {
        # models.CharField: {'widget': TextInput(attrs={'size':'80'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':80})},
        tinymce_models.HTMLField: {"widget": TinyMCE()},
    }
    inlines = [SourceEntryEditHistoryInline]
    save_as = True

    def month_day(self, obj):
        if (obj.low_month):
            display_date = month_abbr[obj.low_month]
            if (obj.low_day):
                display_date += " - " + str(obj.low_day)
            return display_date
    month_day.short_description = 'Mo. Day' 

    def aa_names(self, obj):
        aa_list = ""
        for aa in obj.aa_persons.all():
            aa_list += str(aa.id) + " " + aa.name + ", "
        return aa_list

    def short_pvma(self, obj):
        return obj.pvma_call_num
    short_pvma.short_description = 'pvma'  

    def vol_title(self, obj):
        return obj.volume
    vol_title.short_description = 'vol' 

    # Custom method to render HTML safely
    @admin.display(description='Entry Text')
    def get_entry_text_html(self, obj):
        try:
            html_content = obj.entry_text_html
            if len(html_content) > 75:
                truncated = html_content[:72] + "...</p>"
                return format_html(truncated)
            else:
                return format_html(html_content)
        except Exception as e:
            # Log the error and record ID
            print(f"HTML formatting error in SourceEntry ID: {obj.id}")
            print(f"Error: {str(e)}")
            # Return a safe version of the text or a warning message
            return mark_safe(f'<span style="color:red">HTML Error in Entry ID: {obj.id}</span>')
            # This tells Django to render the HTML safely

    # @admin.display(description='Enslavr')
    # def get_enslaver(self, obj):
    #     try:
    #         enslaver_content = obj.operson_fk
    #         if len(enslaver_content) > 12:
    #             truncated = enslaver_content[:11] + "..."
    #             return truncated
    #         else:
    #             return enslaver_content
    #     except Exception as e:
    #         # Log the error and record ID
    #         print(f"Error: {str(e)}")
    #         return mark_safe(f'<span style="color:red">Error in Entry ID: {obj.id}</span>')

    # From Claude - to make entry_text input wider
    # def formfield_for_dbfield(self, db_field, request, **kwargs):
    #     if db_field.name == 'entry_text':
    #         kwargs['widget'] = forms.TextInput(attrs={'size': '90'})
    #     return super().formfield_for_dbfield(db_field, request, **kwargs)

admin.site.register(PrimarySource, PrimarySourceAdmin)
admin.site.register(Volume, VolumeAdmin)
admin.site.register(SourceType, SourceTypeAdmin)
admin.site.register(SourceEntry, SourceEntryAdmin)
