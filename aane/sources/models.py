from django.core.urlresolvers import reverse
from django.db import models
#from people.models import AAPerson
import people.models

class SourceCollection(models.Model):
	"""docstring for SourceCollection"""
	title = models.CharField(max_length=128, blank=True,  default='')
	description = models.TextField(blank=True,  default='')

	def __str__(self):
		return self.title

class PrimarySource(models.Model):
	"""PrimarySource
	Also includes secondary sources -- determined by source type.
	Originally planned foreign key to Collection, but doens't seem necessary"""
	# .source_collection = models.ForeignKey('SourceCollection')
	source_type = models.CharField(max_length=32, blank=True,  default='')
	title = models.CharField(max_length=128, blank=True,  default='')
	pub_info = models.CharField(max_length=128, blank=True,  default='')
	description = models.TextField(blank=True,  default='')
	year_start = models.IntegerField('Start year or single', default=0)
	year_end = models.IntegerField('End year if range', default=0)
	operson_id = models.IntegerField('O Person id if known',default=0)

	class Meta:
		ordering = ["pk"]
		verbose_name = "Source"
			
	def __str__(self):
		return self.title
		

class SourceEntry(models.Model):
	"""
	SourceEntry
	ForeignKey to PrimarySource
	"""
	primary_source = models.ForeignKey('PrimarySource')
	entry_text = models.CharField(max_length=255)
	clarified = models.CharField(max_length=255, blank=True,  default='')
	aa_id = models.IntegerField('aa id if known for sure',default=0)
	operson_id = models.IntegerField(
							'2ndary person ID, only if aa id not known',default=0)
	name_note = models.CharField('Name note if no id known', max_length=64, 
							blank=True,  default='')
	year_start = models.IntegerField('Start year or single', default=0)
	year_end = models.IntegerField('End year if range', default=0)
	month = models.IntegerField('Month (number)', default=0)
	day = models.IntegerField('Day of month (number)', default=0)
	pvma_call_num = models.CharField(max_length=32, blank=True,  default='')
	date_range = models.CharField('Date range (from title field)', max_length=32, blank=True,  default='')
	page_num = models.CharField('Page info', max_length=32, blank=True,  default='')
	location = models.CharField('Other location info', max_length=32, blank=True,  default='')

	@property
	def aa_name(self):
		aaperson_object = people.models.AAPerson.objects.get(pk=self.aa_id)
		return aaperson_object.name
	
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

