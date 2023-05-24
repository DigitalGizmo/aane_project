from django.contrib import admin
from .models import State, Town

class StateAdmin(admin.ModelAdmin):
    fields = [
        'abbr'
    ]
    list_display = ('abbr',)

class TownAdmin(admin.ModelAdmin):
    fields = [
        'state','title'
    ]
    list_display = ('title', 'state')

admin.site.register(State, StateAdmin)
admin.site.register(Town, TownAdmin)