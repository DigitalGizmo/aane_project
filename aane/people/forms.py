from django import forms
from .models import AAPerson

class PersonSearchForm(forms.Form):
    for_name = forms.CharField(max_length=100, required=False)
    in_bio = forms.CharField(max_length=100, required=False)
    page = forms.IntegerField(required=False)
    tier = forms.IntegerField(required=False)

    # get evidence type list directly from the database
    freedStatus = forms.MultipleChoiceField(
        choices = AAPerson.FREED_STATUS,
        widget  = forms.CheckboxSelectMultiple,
        required=False,
    )

    # order by
    # sortOrder = forms.CharField(max_length=24, required=False)
    SORT_CHOICES = (('name','name'), 
                ('last_name','last name'), 
                ('birth_year','birth'), 
                ('death_year','death'),
                ('first_appearance_year','first rec'),
                ('last_appearance_year','last rec'),
                )
    sortOrder = forms.ChoiceField(
        choices = SORT_CHOICES,
        widget  = forms.Select,
        required=False,
    )

    # # get evidence type list directly from the database
    # tiers = forms.MultipleChoiceField(
    #     choices = AAPerson.TIER,
    #     widget  = forms.RadioSelect,
    #     required=False,
    # )
