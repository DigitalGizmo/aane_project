"""
Export AAPerson data to CSV - keeps HTML but removes line breaks
Run from Django shell: python manage.py shell < export_html_minified.py
"""
import csv
import re
from people.models import AAPerson

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

# Same queryset as your viewset
queryset = AAPerson.objects.filter(
    id__lte=300, 
    research_status__gte=2,
    tier=1
).order_by('name')

fields = [
    'id', 'name', 'first_name', 'last_name', 
    'birth_year', 'death_year', 'gender', 
    'place_of_origin', 'freed_status', 'person_url', 'bio_html'
]

output_file = 'aapeople_export_html.csv'

with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    
    for person in queryset:
        writer.writerow({
            'id': person.id,
            'name': person.name,
            'first_name': person.first_name,
            'last_name': person.last_name,
            'birth_year': person.birth_year or '',
            'death_year': person.death_year or '',
            'gender': person.gender,
            'place_of_origin': person.place_of_origin,
            'freed_status': person.get_freed_status_display(),
            'person_url': person.person_url,
            'bio_html': minify_html(person.bio_html)
        })

print(f'Exported {queryset.count()} records to {output_file}')
