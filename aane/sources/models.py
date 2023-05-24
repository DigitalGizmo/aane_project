from django.urls import reverse
from django.db import models
import people.models

"""
class SourceCollection(models.Model):
    docstring for SourceCollection
    title = models.CharField(max_length=128, blank=True, default='')
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.title
"""
class SourceType(models.Model):
    slug = models.SlugField('short name', max_length=32, unique=True)
    title = models.CharField(max_length=64)
    note = models.TextField(blank=True, default='')   

    def __str__(self):
        return self.title


class PrimarySource(models.Model):
    """PrimarySource
    Also includes secondary sources -- determined by source type.
    Originally planned foreign key to Collection, but doens't seem necessary"""
    # .source_collection = models.ForeignKey('SourceCollection')
    SOURCE_CLASSIFICATION = (
        ('primary','primary'),
        ('secondary','secondary'),
    )
    source_classification = models.CharField('Classification', 
        max_length=32, choices=SOURCE_CLASSIFICATION)
    source_type = models.ForeignKey('SourceType', default=1, 
        on_delete=models.PROTECT)
    location = models.ForeignKey('locations.Town', default=9,
                                 on_delete=models.PROTECT, 
                                 )
    title = models.CharField(max_length=128, blank=True, default='')
    pub_info = models.CharField(max_length=128, blank=True, default='')
    description = models.TextField(blank=True, default='')
    year_start = models.IntegerField('Year', blank=True, null=True, 
        help_text='Start year if range')
    year_end = models.IntegerField('End year', blank=True, null=True,
        help_text='if range')
    operson_id = models.IntegerField('Owner', blank=True, null=True,
        help_text='Id if known')
    scan_id = models.CharField(max_length=32, blank=True, default='',
        help_text='the prefix of the scan name')
    tiff_location = models.CharField(max_length=128, blank=True, null=True)
    # Not used, now per volume
    accession_num = models.CharField(max_length=64, blank=True, null=True,
        help_text='We often do not have this.')
    other_accession_num = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        ordering = ['source_classification', 'title'] # 'source_type', 
        verbose_name = "Source"
    
    @property
    def entries_count(self):
        return self.sourceentry_set.count()

    def __str__(self):
        return self.title


class Volume(models.Model):
    primary_source = models.ForeignKey('PrimarySource', on_delete=models.PROTECT)
    title = models.CharField(max_length=128, blank=True, default='')
    legacy_title = models.CharField(max_length=128, blank=True, default='')
    volume_scan_id = models.CharField(max_length=32, blank=True, default='',
        help_text='if different from primary source scan id')
    year_start = models.IntegerField('Start Year', blank=True, null=True, 
        help_text='Start year if range')
    month_start = models.IntegerField('Start Month', blank=True, null=True, 
        help_text='Optional')
    day_start = models.IntegerField('Start Day', blank=True, null=True)
    year_end = models.IntegerField('End Year', blank=True, null=True,
        help_text='if range')
    month_end = models.IntegerField('End Month', blank=True, null=True)
    day_end = models.IntegerField('End Day', blank=True, null=True)
    accession_num = models.CharField(max_length=64, blank=True, null=True,
        help_text='We often do not have this.')
    other_accession_num = models.CharField(max_length=64, blank=True, null=True,
        help_text='Often the PVMA number')
    note = models.TextField(blank=True, default='')   

    @property
    def two_digit_month_start(self):
        return ("0" + str(self.month_start) 
                if self.month_start < 10 else self.month_start)

    @property
    def two_digit_day_start(self):
        return ("0" + str(self.day_start) 
                if self.day_start < 10 else self.day_start)

    @property
    def two_digit_month_end(self):
        return ("0" + str(self.month_end) 
                if self.month_end < 10 else self.month_end)

    @property
    def two_digit_day_end(self):
        return ("0" + str(self.day_end) 
                if self.day_end < 10 else self.day_end)

    def __str__(self):
        return self.primary_source.title + ": " + self.title

    class Meta:
        ordering = ['primary_source', 'year_start', 'title'] # 'source_type', 

class SourceEntry(models.Model):
    """
    SourceEntry
    Has foreignKey to PrimarySource
    All entries will end up with an aa_id - lots of those ids will be more or less place-
    holders. In the meantime, an entry may have no aa_id, in which case the name_note will 
    be displayed.
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
    IMAGE_STATUS = (
        (0, 'TBD'),
        (1, 'NotFound'),
        (2, 'NoImg'),
        (3, 'Scanned'),
        (5, 'Cnvrted'),
        (6, 'Posted'),
        (7, 'Hilite'),
    )
    DATA_STATUS = (
        (0, 'OrigEntry'),
        (1, 'NewEntry'),
        (2, 'Updated'),
        (3, 'Vetted'),
    )
    primary_source = models.ForeignKey('PrimarySource', on_delete=models.PROTECT,
        help_text='We will soon go by volume only')
    volume = models.ForeignKey('Volume', on_delete=models.PROTECT,
        null=True, blank=True)
    entry_text = models.CharField(max_length=255)
    clarified = models.CharField(max_length=255, blank=True, default='',
        help_text='was for editor interpretation of entry text')
    event = models.CharField(max_length=128, blank=True, default='')
    aa_id = models.IntegerField(blank=True, null=True,
        help_text="Only if known for sure")
    operson_id = models.IntegerField(
        'Owner ID', blank=True, null=True, 
        help_text="blank if free. If unknown, choose the special 'Unknow Owner'")
    name_note = models.CharField(max_length=64, 
        blank=True, default='', help_text='If person ID is not known')
    date_status = models.IntegerField(default=0, choices=DATE_STATUS)
    low_year = models.IntegerField('Year', blank=True, null=True,
        help_text='Low year if range')
    low_month = models.IntegerField('Month', choices=LOW_MONTH, blank=True, null=True)
    low_day = models.IntegerField('Day', blank=True, null=True,
        help_text='number')
    upr_year = models.IntegerField('Upper year if range', blank=True, null=True)
    upr_month = models.IntegerField('Month', blank=True, null=True)
    upr_day = models.IntegerField('Day', blank=True, null=True,
        help_text='upper range')
    date_note = models.CharField(max_length=124, blank=True, default='')
    pvma_call_num = models.CharField(max_length=32, blank=True, default='')
    date_range = models.CharField(max_length=32, blank=True, default='')
    vol_book = models.CharField('Volume or book info', max_length=32, blank=True, default='')
    page_num = models.CharField(max_length=64, blank=True, default='')
    transaction_note = models.CharField(max_length=64, blank=True, default='')
    dollars = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    pounds = models.IntegerField(blank=True, null=True)
    shillings = models.IntegerField(blank=True, null=True)
    pence = models.IntegerField(blank=True, null=True)
    farthing = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, default='')
    legacy_enslaved_id = models.IntegerField(blank=True, null=True)
    access_order = models.IntegerField(blank=True, null=True)
    legacy_id = models.IntegerField(blank=True, null=True)
    image_name = models.CharField(max_length=128, blank=True, null=True)
    scan_name = models.CharField(max_length=128, blank=True, null=True)
    percent_top = models.IntegerField('% from top', blank=True, null=True)
    percent_height = models.IntegerField('% height', blank=True, null=True)
    percent_left = models.IntegerField('% from left', blank=True, null=True)
    percent_right = models.IntegerField('% width', blank=True, null=True)
    page_note = models.TextField(blank=True, default='')
    scan_date = models.CharField(max_length=24, blank=True, null=True)
    image_source = models.CharField(max_length=255, blank=True, default='')
    other_image_source = models.CharField(max_length=128, blank=True, default='')
    scan_note = models.TextField(blank=True, default='')
    data_status = models.IntegerField('data', default=0, choices=DATA_STATUS,
        help_text='Data Status')
    image_status = models.IntegerField('image', default=0, choices=IMAGE_STATUS,
        help_text='Image Status')

    class Meta:
        ordering = ['primary_source', 'volume', 'low_year', 
        'low_month', 'low_day']
             
    @property
    def aa_person(self):
        return people.models.AAPerson.objects.get(pk=self.aa_id)
    
    @property
    def o_person(self):
        return people.models.OPerson.objects.get(pk=self.operson_id)
    
    # so that generic update and create views can find the detail template.
    def get_absolute_url(self):
        return reverse('sources:entry_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.entry_text

class VolumeIdImport(models.Model):
    legacy_id = models.IntegerField(blank=True, null=True)
    volume_id = models.IntegerField(blank=True, null=True)

class EntryScanImport(models.Model):
    legacy_id = models.IntegerField(blank=True, null=True)
    scan_date = models.CharField(max_length=24, blank=True, default='')
    image_source = models.CharField(max_length=255, blank=True, default='')
    other_image_source = models.CharField(max_length=128, blank=True, default='')
    scan_name = models.CharField(max_length=128, blank=True, null=True)
    scan_note = models.TextField(blank=True, default='')
