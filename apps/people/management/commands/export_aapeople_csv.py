"""
Django management command to export AAPerson data to CSV
Place this file in: people/management/commands/export_aapeople_csv.py

Run with: python manage.py export_aapeople_csv
"""
import csv
import re
from django.core.management.base import BaseCommand
from people.models import AAPerson


def strip_html_and_normalize(html_text):
    """Remove HTML tags and normalize whitespace"""
    # Remove class attributes from all tags
    text = re.sub(r'\s+class="[^"]*"', '', html_text)
    text = re.sub(r"\s+class='[^']*'", '', text)
    
    # Remove span tags (both opening and closing) but keep content
    text = re.sub(r'<span[^>]*>', '', text)
    text = re.sub(r'</span>', '', text)
    
    # Remove all remaining HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Replace multiple whitespace (including newlines) with single space
    text = re.sub(r'\s+', ' ', text)
    
    # Strip leading/trailing whitespace
    return text.strip()


def minify_html(html_text):
    """Remove line breaks, extra whitespace, class attributes, and span tags from HTML but keep other tags"""
    # Remove class attributes from all tags
    text = re.sub(r'\s+class="[^"]*"', '', html_text)
    text = re.sub(r"\s+class='[^']*'", '', text)
    
    # Remove span opening tags (with any attributes)
    text = re.sub(r'<span[^>]*>', '', text)
    
    # Remove span closing tags
    text = re.sub(r'</span>', '', text)
    
    # Replace newlines and multiple spaces with single space
    text = re.sub(r'\s+', ' ', text)
    
    # Strip leading/trailing whitespace
    return text.strip()


class Command(BaseCommand):
    help = 'Export AAPerson data to CSV'

    def add_arguments(self, parser):
        parser.add_argument(
            '--output',
            type=str,
            default='aapeople_export.csv',
            help='Output filename (default: aapeople_export.csv)'
        )
        parser.add_argument(
            '--limit',
            type=int,
            default=None,
            help='Limit number of records (default: all matching records)'
        )
        parser.add_argument(
            '--keep-html',
            action='store_true',
            help='Keep HTML tags (default: strip HTML and normalize to plain text)'
        )

    def handle(self, *args, **options):
        output_file = options['output']
        limit = options['limit']
        keep_html = options['keep_html']
        
        # Use the same queryset as your AAPersonViewSet
        queryset = AAPerson.objects.filter(
            id__lte=300, 
            research_status__gte=2,
            tier=1
        ).order_by('name')
        
        if limit:
            queryset = queryset[:limit]
        
        # Define the fields you want to export (matching your serializer)
        field_name = 'bio_html' if keep_html else 'bio_text'
        fields = [
            'id',
            'name',
            'first_name',
            'last_name',
            'birth_year',
            'death_year',
            'gender',
            'place_of_origin',
            'freed_status',
            'person_url',
            field_name
        ]
        
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            
            count = 0
            for person in queryset:
                if keep_html:
                    bio_value = minify_html(person.bio_html)
                else:
                    bio_value = strip_html_and_normalize(person.bio_html)
                
                row = {
                    'id': person.id,
                    'name': person.name,
                    'first_name': person.first_name,
                    'last_name': person.last_name,
                    'birth_year': person.birth_year or '',
                    'death_year': person.death_year or '',
                    'gender': person.gender,
                    'place_of_origin': person.place_of_origin,
                    'freed_status': person.get_freed_status_display(),  # Get human-readable value
                    'person_url': person.person_url,
                    field_name: bio_value
                }
                writer.writerow(row)
                count += 1
            
            self.stdout.write(
                self.style.SUCCESS(f'Successfully exported {count} records to {output_file}')
            )
