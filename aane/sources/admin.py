from django.contrib import admin
from .models import SourceCollection, PrimarySource, SourceEntry


class SourceCollectionAdmin(admin.ModelAdmin):
	fields = ['title','sec_person_id']
	list_display = ('title', 'sec_person_id')
admin.site.register(SourceCollection, SourceCollectionAdmin)

class SourceEntryInline(admin.StackedInline):
    model = SourceEntry
    extra = 3

class PrimarySourceAdmin(admin.ModelAdmin):
	fields = ['source_collection', 'title','pvma_call_num','description','year_start', 'year_end']
	inlines = [SourceEntryInline]
	list_display = ('title', 'pvma_call_num')
admin.site.register(PrimarySource, PrimarySourceAdmin)

class SourceEntryAdmin(admin.ModelAdmin):
	fields = ['primary_source', 'entry_text', 'clarified', 'aa_id', 'secondary_person_id', 'name_note']
	list_display = ('entry_text', 'aa_id', 'secondary_person_id')
	list_filter	 = ['primary_source'] 
admin.site.register(SourceEntry, SourceEntryAdmin)
