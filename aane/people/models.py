from django.urls import reverse
from django.db import models
from django_quill.fields import QuillField
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
    birth_year = models.IntegerField(blank=True, null=True)
    death_year = models.IntegerField(blank=True, null=True)
    locations = models.ManyToManyField('locations.Town', blank=True)
    research_status = models.IntegerField(default=2, choices=RESEARCH_STATUS)
    note = models.TextField(blank=True, default='')   

    class Meta:
        abstract = True

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
    FREED_STATUS = (
        (1,'enslaved'),
        (2,'enslaved, then free'),
        (3,'always free'),
    )
    alt_name_spelling = models.CharField(max_length=32, blank=True, default='')
    freed_name = models.CharField(max_length=32, blank=True, default='')
    first_appearance_year = models.IntegerField(blank=True, null=True)
    last_appearance_year = models.IntegerField(blank=True, null=True)
    free_start_year = models.IntegerField(blank=True, null=True)
    owner_id = models.IntegerField(blank=True, null=True)
    place_of_origin = models.CharField(max_length=64, blank=True, default='')
    owners = models.ManyToManyField('people.OPerson', verbose_name='Owner(s)', 
        blank=True)
    known_status = models.IntegerField(default=0, choices=KNOWN_STATUS)
    freed_status = models.IntegerField(default=0, choices=FREED_STATUS)

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
        ('user','user'),
        ('service_provider', 'service_provider'),
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
        ordering = ["pk"]
        verbose_name = "Others/Enslavers"

