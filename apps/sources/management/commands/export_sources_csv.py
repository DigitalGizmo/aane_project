"""
Django management command to export SourceEntry data to CSV

Run with: python manage.py export_sources_csv
Output goes to: exports/source_entries_export.csv
"""
import csv
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from sources.models import SourceEntry


class Command(BaseCommand):
    help = 'Export SourceEntry data to CSV'

    def add_arguments(self, parser):
        parser.add_argument(
            '--output',
            type=str,
            default='source_entries_export.csv',
            help='Output filename (default: source_entries_export.csv)'
        )
        parser.add_argument(
            '--limit',
            type=int,
            default=40,
            help='Limit number of records (default: 40)'
        )
        parser.add_argument(
            '--increment',
            type=int,
            default=1,
            help='Sample every Nth record (default: 1, i.e. every record)'
        )

    def handle(self, *args, **options):
        output_file = options['output']
        limit = options['limit']
        increment = options['increment']

        # Get sampled IDs first (every Nth record)
        all_ids = list(
            SourceEntry.objects.filter(
                data_status__gte=0
            ).order_by('id').values_list('id', flat=True)
        )
        sampled_ids = all_ids[::increment][:limit]

        # Optimized queryset with related data for sampled records
        queryset = SourceEntry.objects.select_related(
            'volume__primary_source__source_type',
            'volume__primary_source__location__state',
            'operson_fk'
        ).prefetch_related(
            'aa_persons'
        ).filter(
            id__in=sampled_ids
        ).order_by('id')

        # Define CSV fields
        fields = [
            'Month',
            'Year',
            'LASTNAME',
            'FirstName',
            'RecordType',
            'EnslaverLastName',
            'EnslaverFirstName',
            'City',
            'State',
            'Source',
            'URL',
            'Notes'
        ]

        # Ensure exports directory exists
        exports_dir = os.path.join(settings.BASE_DIR, 'exports')
        os.makedirs(exports_dir, exist_ok=True)
        output_path = os.path.join(exports_dir, output_file)

        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()

            count = 0
            for entry in queryset:
                # Get first aa_person (may be None)
                aa_person = entry.aa_persons.first()

                # Get location safely
                primary_source = entry.volume.primary_source
                location = primary_source.location if primary_source else None

                row = {
                    'Month': entry.get_low_month_display() if entry.low_month else '',
                    'Year': entry.low_year or '',
                    'LASTNAME': aa_person.last_name.upper() if aa_person and aa_person.last_name else '',
                    'FirstName': aa_person.first_name if aa_person else '',
                    'RecordType': primary_source.source_type.title if primary_source and primary_source.source_type else '',
                    'EnslaverLastName': entry.operson_fk.last_name if entry.operson_fk else '',
                    'EnslaverFirstName': entry.operson_fk.first_name if entry.operson_fk else '',
                    'City': location.title if location else '',
                    'State': location.state.abbr if location and location.state else '',
                    'Source': primary_source.title if primary_source else '',
                    'URL': f'https://aane.deerfield-ma.org/sources/entry/{entry.id}/',
                    'Notes': entry.entry_text_html or ''
                }
                writer.writerow(row)
                count += 1

            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully exported {count} records to {output_path} '
                    f'(sampled every {increment} of {len(all_ids)} total)'
                )
            )
