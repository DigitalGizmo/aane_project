from django.urls import reverse
from django.db import models
from django_quill.fields import QuillField
from tinymce import models as tinymce_models
from django.contrib import admin
from sources.models import SourceEntry


class PersonModel(models.Model):
    """
    Person - abstract class for fields common to AAPerson and 
    OPerson (Other, Owner)
    """
    GENDER = (
        ('male','male'),
        ('female','female'),
        ('unknown', 'unknown'),
    )
    RESEARCH_STATUS = (
        (0,'delete'),
        (1,'inactive'),
        (2,'needs research'),
        (3,'in progress'),
        # (4,'problematic'),
        (6,'publishable'),
    )    
    name = models.CharField(max_length=64)
    first_name = models.CharField(max_length=32, blank=True, default='')
    last_name = models.CharField(max_length=32, blank=True, default='')
    gender = models.CharField(max_length=12, choices=GENDER)
    bio = QuillField(blank=True, default='')
    bio_plain_text = models.TextField(blank=True, default='')
    full_bio = QuillField(blank=True, default='')
    bio_html = tinymce_models.HTMLField('bio text', blank=True, default='')
    birth_year = models.IntegerField(blank=True, null=True)
    death_year = models.IntegerField(blank=True, null=True)
    locations = models.ManyToManyField('locations.Town', blank=True)
    research_status = models.IntegerField(default=2, choices=RESEARCH_STATUS)
    note = models.TextField(blank=True, default='')
    is_birth_circa = models.BooleanField('circa', default=False)  
    is_death_circa = models.BooleanField('circa', default=False)  

    class Meta:
        abstract = True

    # Courtesy of Clause 3.5 Sonnet
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(
            first_location=models.Min('locations__title')
        ).order_by('first_location')
    
    @admin.display(description='Locations', ordering='first_location')
    def get_locations(self):
        return ", ".join([str(location) for location in self.locations.all()])

    def __str__(self):
        birth = " "
        if self.birth_year: birth = str(self.birth_year)
        death = " "
        if self.death_year: death = str(self.death_year)
        return str(self.id) + " " + self.name + " " + birth + " - " + death


class AAPerson(PersonModel):
    """
    AAPerson - inherits PersonModel
    """
    KNOWN_STATUS = (
        (1,'known'),
        (2,'only ownr'),
        (3,'unknown'),
        (9,'discard'),
    )
    CONFIDENCE = (
        (1,'confirmed identity'),
        (2,'only enslaver known'),
        (3,'indeterminate'),
        (4,'possible duplicate'),
    )
    FREED_STATUS = (
        (1,'enslaved'),
        (2,'enslaved, then free'),
        (3,'always free'),
        (4,'unknown')
    )
    TIER = (
        (0,'other people'),
        (1,'core people'),
    )
    alt_name_spelling = models.CharField(max_length=128, blank=True, default='')
    freed_name = models.CharField(max_length=32, blank=True, default='')
    first_appearance_year = models.IntegerField(blank=True, null=True)
    last_appearance_year = models.IntegerField(blank=True, null=True)
    free_start_year = models.IntegerField(blank=True, null=True)
    owner_id = models.IntegerField('Legacy owner ID', blank=True, null=True)
    place_of_origin = models.CharField('Birthplace, if known',
        max_length=64, blank=True, default='')
    owners = models.ManyToManyField('people.OPerson', verbose_name='Enslaver(s)', 
        blank=True)
    known_status = models.IntegerField(default=0, choices=KNOWN_STATUS)
    freed_status = models.IntegerField(default=0, choices=FREED_STATUS)
    confidence = models.IntegerField('Confidence Level',choices=CONFIDENCE, 
                                     blank=True, null=True)
    tier = models.IntegerField(default=0, choices=TIER)

    class Meta:
        ordering = ['name'] #'known_status', 'freed_status', 
        verbose_name = "African American"
    	
    # return list of entries for given person
    # Will be obsolete when sources.aa_persons is fully implemented
    # @property
    # def person_entries(self):
    #     person_entry_list = SourceEntry.objects.filter(aa_id=self.pk)
    #     return person_entry_list

    # Just for the aaperson list number of entries per
    @property
    def person_entries_count(self):
        aaperson_entry_list = self.aa_persons
        return aaperson_entry_list.count()

    # so that generic update and create views can find the detail template.
    def get_absolute_url(self):
        return reverse('people:aaperson_detail', kwargs={'pk': self.pk})
		

class OPerson(PersonModel):
    """
    OPerson Other/ Owner - inherits PersonModel
    """
    ROLE = (
        ('owner','enslaver'),
        ('user', 'service consumer'),
        ('service_provider', 'service provider'),
        ('former', 'former enslaver'),
    )
    RACE = (
        ('white','white'),
        ('african_american','african_american'),
        ('native', 'native'),
    )
    title = models.CharField(max_length=24, blank=True, default='')
    role = models.CharField(max_length=24, choices=ROLE)
    race = models.CharField(max_length=24, choices=RACE)
    year_lower = models.IntegerField(blank=True, null=True)
    year_upper = models.IntegerField(blank=True, null=True)
    legacy_owner_id = models.IntegerField(blank=True, null=True)
    original_id = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ["last_name"]
        verbose_name = "Others/Enslavers"

