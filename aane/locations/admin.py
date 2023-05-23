from django.contrib import admin
from .models import State

class StateAdmin(admin.ModelAdmin):
    fields = [
        'abbr'
    ]
    list_display = ('abbr',)


admin.site.register(State, StateAdmin)