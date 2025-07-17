from django.urls import reverse
from django.db import models
from tinymce import models as tinymce_models
# from tinymce.models import HTMLField
from django.utils.html import format_html, strip_tags
import re
from django.utils.safestring import mark_safe
import people.models
from sitewide.models import CommonEditHistory

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

    class Meta:
        ordering = ['title']  

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
    @property
    def active_entries(self):
        return self.sourceentry_set.filter(data_status__gte=0)

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
        (-2, 'To Delete'),
        (-1, 'Inactive'),
        (0, 'Orig Entry'),
        (1, 'New Entry'),
        (2, 'Updated'),
        (3, 'Vetted'),
    )
    primary_source = models.ForeignKey('PrimarySource', on_delete=models.PROTECT,
        help_text='We will soon go by volume only')
    volume = models.ForeignKey('Volume', on_delete=models.PROTECT,
        null=True, blank=True)
    entry_text = models.CharField(max_length=255)
    entry_text_html = tinymce_models.HTMLField(blank=True, default='')
    interpretive_note = tinymce_models.HTMLField(blank=True, default='')
    clarified = models.CharField(max_length=255, blank=True, default='',
        help_text='was for editor interpretation of entry text')
    event = models.CharField(max_length=128, blank=True, default='')
    aa_id = models.IntegerField('legacy aa_id', blank=True, null=True)
    aa_id_legacy = models.IntegerField(blank=True, null=True,
        help_text="Legacy aa_id unaltered")
    operson_id = models.IntegerField(
        'Legacy Enslaver ID', blank=True, null=True)
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
    transaction_note = models.CharField('Legacy transaction note',
        max_length=64, blank=True, default='')
    dollars = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    pounds = models.IntegerField(blank=True, null=True)
    shillings = models.IntegerField(blank=True, null=True)
    pence = models.DecimalField(max_digits=4, decimal_places=1,blank=True, null=True)
    farthing = models.IntegerField(blank=True, null=True)
    notes = models.TextField('Internal Notes', blank=True, default='')
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
    aa_persons = models.ManyToManyField('people.AAPerson', 
        related_name='aa_persons', blank=True)
    operson_fk = models.ForeignKey('people.OPerson', on_delete=models.PROTECT,
    verbose_name='Enslaver', null=True, blank=True)

    class Meta:
        ordering = ['primary_source', 'volume', 'low_year', 
        'low_month', 'low_day']
             
    @property
    def aa_person(self):
        return people.models.AAPerson.objects.get(pk=self.aa_id)
    
    @property
    def o_person(self):
        # Updated July 2024 to reference the foreign key operson
        return people.models.OPerson.objects.get(pk=self.operson_fk_id)
    
    @property
    def safe_entry_html(self):
        """
        Returns the entry HTML with <p> tags stripped for safe display.
        Used in templates where full content is needed.
        """
        try:
            html_content = self.entry_text_html
            # Strip opening and closing <p> tags
            if html_content.startswith('<p>') and html_content.endswith('</p>'):
                return html_content[3:-4]
            return html_content
        except Exception as e:
            print(f"HTML processing error in SourceEntry ID: {self.id}")
            print(f"Error: {str(e)}")
            return f'<span style="color:red">HTML Error in Entry ID: {self.id}</span>'

    @property
    def truncated_entry_html(self, length=72):
        """
        Returns truncated HTML content for display in lists.
        Default length is 72 characters to match current admin display.
        This version is HTML-aware and won't break tags.
        """
        try:
            html_content = self.safe_entry_html  # Use the safe version
            return self._smart_truncate_html(html_content, length)
        except Exception as e:
            print(f"HTML truncation error in SourceEntry ID: {self.id}")
            print(f"Error: {str(e)}")
            return f'<span style="color:red">HTML Error in Entry ID: {self.id}</span>'


    def get_truncated_html(self, length=72):
        """
        Method version that allows custom length specification.
        Useful when different views need different truncation lengths.
        This version is HTML-aware and won't break tags.
        """
        try:
            html_content = self.safe_entry_html
            return self._smart_truncate_html(html_content, length)
        except Exception as e:
            print(f"HTML truncation error in SourceEntry ID: {self.id}")
            print(f"Error: {str(e)}")
            return f'<span style="color:red">HTML Error in Entry ID: {self.id}</span>'

    def _smart_truncate_html(self, html_content, length):
        """
        Helper method that truncates HTML content without breaking tags.
        
        Args:
            html_content: The HTML string to truncate
            length: The maximum length (counting only visible text)
        
        Returns:
            Truncated HTML that doesn't break any tags
        """
        if not html_content:
            return html_content
        
        # First check if the plain text is already short enough
        plain_text = strip_tags(html_content)
        if len(plain_text) <= length:
            return html_content
        
        # Pattern to match HTML tags and text separately
        tag_pattern = re.compile(r'(<[^>]+>)|([^<]+)')
        
        parts = []
        text_length = 0
        truncated = False
        
        for match in tag_pattern.finditer(html_content):
            tag, text = match.groups()
            
            if tag:
                # It's an HTML tag, add it without counting length
                parts.append(tag)
            elif text:
                # It's text content
                if text_length + len(text) <= length:
                    # We can add all of this text
                    parts.append(text)
                    text_length += len(text)
                else:
                    # We need to truncate this text
                    remaining = length - text_length
                    if remaining > 0:
                        # Truncate at word boundary if possible
                        truncated_text = text[:remaining]
                        # Try to find the last complete word
                        last_space = truncated_text.rfind(' ')
                        if last_space > remaining * 0.7:  # Only use word boundary if we're not losing too much
                            truncated_text = truncated_text[:last_space]
                        parts.append(truncated_text)
                    truncated = True
                    break
        
        # If we truncated, we need to close any open tags
        if truncated:
            result = ''.join(parts)
            # Find all opening tags and their corresponding closing tags
            open_tags = []
            tag_pattern = re.compile(r'<(/?)(\w+)[^>]*>')
            
            for match in tag_pattern.finditer(result):
                is_closing, tag_name = match.groups()
                if is_closing:
                    # Remove the corresponding opening tag if it exists
                    if open_tags and open_tags[-1] == tag_name:
                        open_tags.pop()
                else:
                    # Check if it's not a self-closing tag
                    if tag_name.lower() not in ['br', 'hr', 'img', 'input', 'meta', 'link']:
                        open_tags.append(tag_name)
            
            # Close any remaining open tags in reverse order
            for tag in reversed(open_tags):
                result += f'</{tag}>'
            
            result += '...'
            return result
        else:
            return ''.join(parts)

    # so that generic update and create views can find the detail template.
    def get_absolute_url(self):
        return reverse('sources:entry_detail', kwargs={'pk': self.pk})

    def __str__(self):
        """
        Updated to use the new truncated property
        """
        try:
            # Using format_html to ensure it's marked safe
            return format_html(self.truncated_entry_html)
        except Exception as e:
            print(f"HTML formatting error in SourceEntry ID: {self.id}")
            print(f"Error: {str(e)}")
            return mark_safe(f'<span style="color:red">HTML Error in Entry ID: {self.id}</span>')
        
class SourceEntryEditHistory(CommonEditHistory):
    source_entry = models.ForeignKey('SourceEntry', related_name='source_entries',
                on_delete=models.CASCADE)


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

class AAIDImport(models.Model):
    entry_id = models.IntegerField()
    aa_id = models.IntegerField()
