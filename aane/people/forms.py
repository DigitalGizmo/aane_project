from django import forms
from .models import AAPerson

class PersonSearchForm(forms.Form):
    q = forms.CharField(max_length=100, required=False)
    page = forms.IntegerField(required=False)

    # get evidence type list directly from the database
    freedStatus = forms.MultipleChoiceField(
        choices = AAPerson.FREED_STATUS,
        widget  = forms.CheckboxSelectMultiple,
        required=False,
    )
