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
    list_display = ('title', 'id', 'source_type', 'pub_info', 'operson_id', 'year_start', 'year_end')
    search_fields = ['title']
    list_filter  = ['source_type'] 
admin.site.register(PrimarySource, PrimarySourceAdmin)

class SourceEntryAdmin(admin.ModelAdmin):
    fields = ['primary_source', 'entry_text', 'clarified', 'aa_id', 
        'operson_id', 'name_note', 'year_start', 'year_end', 'month', 'day',
        'pvma_call_num', 'date_range', 'page_num', 'location']
    list_display = ('entry_text', 'aa_id', 'operson_id')
    list_filter  = ['primary_source'] 
admin.site.register(SourceEntry, SourceEntryAdmin)
