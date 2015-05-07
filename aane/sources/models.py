from django.core.urlresolvers import reverse
from django.db import models
#from people.models import AAPerson
import people.models

"""
class SourceCollection(models.Model):
    docstring for SourceCollection
    title = models.CharField(max_length=128, blank=True, default='')
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.title
"""

class PrimarySource(models.Model):
    """PrimarySource
    Also includes secondary sources -- determined by source type.
    Originally planned foreign key to Collection, but doens't seem necessary"""
    # .source_collection = models.ForeignKey('SourceCollection')
    SOURCE_TYPE = (
        ('primary','primary'),
        ('secondary','secondary'),
    )
    source_type = models.CharField(max_length=32, choices=SOURCE_TYPE)
    title = models.CharField(max_length=128, blank=True, default='')
    pub_info = models.CharField(max_length=128, blank=True, default='')
    description = models.TextField(blank=True, default='')
    year_start = models.IntegerField('Start year or single', blank=True, null=True)
    year_end = models.IntegerField('End year if range', blank=True, null=True)
    operson_id = models.IntegerField('O Person id if known', blank=True, null=True)

    class Meta:
        ordering = ["pk"]
        verbose_name = "Source"
            
    def __str__(self):
        return self.title
        

class SourceEntry(models.Model):
    """
    SourceEntry
    Has foreignKey to PrimarySource
    Fields:
        If we want to display shillings or pence as fractions we'll need
        calculate from the integer fields.
    """
    DATE_STATUS = (
        (0, 'As written'),
        (1, 'Before'),
        (2, 'After'),
        (3, 'Uncertain'),
        (4, 'Unknown'),
    )
    LOW_MONTH = (
        (1, 'Jan'),
        (2, 'Feb'),
        (3, 'Mar'),
        (4, 'Apr'),
        (5, 'May'),
        (6, 'Jun'),
        (7, 'Jul'),
        (8, 'Aug'),
        (9, 'Sep'),
        (10, 'Oct'),
        (11, 'Nov'),
        (12, 'Dec'),
    )
    primary_source = models.ForeignKey('PrimarySource')
    entry_text = models.CharField(max_length=255)
    clarified = models.CharField(max_length=255, blank=True, default='')
    event = models.CharField(max_length=128, blank=True, default='')
    aa_id = models.IntegerField('aa id if known for sure', blank=True, null=True)
    operson_id = models.IntegerField(
        'Owner ID', blank=True, null=True, 
        help_text="blank if free. If unknown, choose the special 'Unknow Owner")
    name_note = models.CharField('Name note if no id known', max_length=64, 
        blank=True, default='')
    date_status = models.IntegerField(default=0, choices=DATE_STATUS)
    low_year = models.IntegerField('Lower year or single', blank=True, 
        null=True)
    low_month = models.IntegerField('Month (number)', choices=LOW_MONTH, blank=True, null=True)
    low_day = models.IntegerField('Day of month (number)', blank=True, null=True)
    upr_year = models.IntegerField('Upper year if range', blank=True, null=True)
    upr_month = models.IntegerField('Month (number)', blank=True, null=True)
    upr_day = models.IntegerField('Day of month (number)', blank=True, null=True)
    date_note = models.CharField(max_length=124, blank=True, default='')
    pvma_call_num = models.CharField(max_length=32, blank=True, default='')
    date_range = models.CharField('Date range (from title field)', max_length=32, 
        blank=True, default='')
    vol_book = models.CharField('Volume or book info', max_length=32, blank=True, default='')
    page_num = models.CharField('Page info', max_length=64, blank=True, default='')
    transaction_note = models.CharField(max_length=64, blank=True, default='')
    dollars = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    pounds = models.IntegerField(blank=True, null=True)
    shillings = models.IntegerField(blank=True, null=True)
    pence = models.IntegerField(blank=True, null=True)
    farthing = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, default='')
    legacy_enslaved_id = models.IntegerField(blank=True, null=True)
    access_order = models.IntegerField(blank=True, null=True)
    legacy_id = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['low_year', 'low_month', 'low_day']
             
    @property
    def aa_person(self):
        return people.models.AAPerson.objects.get(pk=self.aa_id)
    
    @property
    def o_name(self):
        operson_object = people.models.OPerson.objects.get(pk=self.operson_id)
        return operson_object.name
    
    @property
    def o_person(self):
        return people.models.OPerson.objects.get(pk=self.operson_id)
    
    @property
    def aa_id_status(self):
        id_status ="ambiguous"
        if self.enslaved_id > 0:
            id_status = "known"
        elif self.owner_id > 0:
            id_status = "owner known"
        return id_status

    @property
    def person_entries_test(self):
        return "test string"
    
    # so that generic update and create views can find the detail template.
    def get_absolute_url(self):
        return reverse('sources:entry_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.entry_text

