from django import forms
from .models import SourceType


class SourceSearchForm(forms.Form):
    q = forms.CharField(max_length=100, required=False)
    page = forms.IntegerField(required=False)

    # get evidence type list directly from the database
    sourceTypes = forms.MultipleChoiceField(
        choices = SourceType.objects.all().values_list('slug', 
            'title').order_by('title'),
        widget  = forms.CheckboxSelectMultiple,
        required=False,
    )

class EntrySearchForm(forms.Form):
    q = forms.CharField(max_length=100, required=False)
    year = forms.CharField(max_length=100, required=False)
    page = forms.IntegerField(required=False)

    # # get evidence type list directly from the database
    # sourceTypes = forms.MultipleChoiceField(
    #     choices = SourceType.objects.all().values_list('slug', 
    #         'title').order_by('title'),
    #     widget  = forms.CheckboxSelectMultiple,
    #     required=False,
    # )
