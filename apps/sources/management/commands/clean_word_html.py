"""
Django management command to strip Word/Office markup out of SourceEntry.entry_text_html,
leaving nothing but <p>, <br> and the inline emphasis tags.

Transcript lines that Word wrote as separate paragraphs are rejoined into one <p>
with <br> between them, so they set tight rather than with paragraph spacing.
A blank line in the source starts a new <p>. Use --keep-paragraphs to opt out.

Dry run (default - shows before/after, changes nothing):
    python manage.py clean_word_html

Write the changes:
    python manage.py clean_word_html --apply

Target specific rows instead of the 'mso' search:
    python manage.py clean_word_html --ids 1234,1235 --apply
"""
import re
from html.parser import HTMLParser

from django.core.management.base import BaseCommand
from sources.models import SourceEntry

# Long &nbsp; runs (fake tab stops) collapse to this
TAB_RUN = '&nbsp;' * 4


class WordHtmlCleaner(HTMLParser):
    """Keeps a small tag whitelist (attribute-free), drops every other tag but keeps its text."""
    KEEP = {'p', 'b', 'i', 'em', 'strong', 'u'}   # paired tags
    VOID = {'br'}                                 # no closing tag

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in self.VOID or tag in self.KEEP:
            self.parts.append(f'<{tag}>')

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag):
        if tag in self.KEEP:
            self.parts.append(f'</{tag}>')

    def handle_data(self, data):
        # ordinary whitespace collapses; \xa0 (&nbsp;) is handled after escaping
        data = re.sub(r'[ \t\r\n]+', ' ', data)
        data = data.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        data = re.sub('\xa0{2,}', TAB_RUN, data)
        data = data.replace('\xa0', ' ')
        self.parts.append(data)

    def result(self):
        return ''.join(self.parts)


def is_blank(line):
    """A line holding nothing but spacing - Word's way of writing a blank line."""
    return not re.sub(r'(&nbsp;|<br>|\s)+', '', line)


def clean_html(raw, join_lines=True):
    parser = WordHtmlCleaner()
    parser.feed(raw)
    parser.close()
    out = parser.result()

    # source newlines between paragraphs, and padding just inside a paragraph.
    # (whitespace between inline tags is left alone - it is real word spacing)
    out = re.sub(r'</p>\s+<p>', '</p><p>', out)
    out = re.sub(r'<p>\s+', '<p>', out)
    out = re.sub(r'\s+</p>', '</p>', out)
    # adjacent tab runs (one per original <span>) merge into a single run
    out = re.sub(r'(?:&nbsp;|\s)*(?:&nbsp;)(?:&nbsp;|\s)*', TAB_RUN, out)
    out = re.sub(r' {2,}', ' ', out)

    lines = re.findall(r'<p>(.*?)</p>', out, re.S)
    if not lines:
        return out.strip()

    if not join_lines:
        return '\n'.join(f'<p>{line}</p>' for line in lines if not is_blank(line))

    # Word writes every transcript line as its own paragraph. Rejoin them with <br>
    # so they set tight, and start a new <p> only where a blank line was.
    blocks, current = [], []
    for line in lines:
        if is_blank(line):
            if current:
                blocks.append(current)
                current = []
        else:
            current.append(line)
    if current:
        blocks.append(current)

    return '\n'.join('<p>' + '\n<br>'.join(block) + '</p>' for block in blocks)


class Command(BaseCommand):
    help = 'Strip Word markup from SourceEntry.entry_text_html, leaving only <p> and <br>'

    def add_arguments(self, parser):
        parser.add_argument(
            '--ids',
            type=str,
            default=None,
            help='Comma-separated SourceEntry ids (default: search for --match)'
        )
        parser.add_argument(
            '--match',
            type=str,
            default='mso',
            help="Substring identifying bad entries (default: 'mso')"
        )
        parser.add_argument(
            '--apply',
            action='store_true',
            help='Save the changes (default is a dry run)'
        )
        parser.add_argument(
            '--keep-paragraphs',
            action='store_true',
            help='Leave every source line in its own <p> instead of joining with <br>'
        )

    def handle(self, *args, **options):
        if options['ids']:
            ids = [int(i) for i in options['ids'].split(',')]
            entries = SourceEntry.objects.filter(pk__in=ids)
        else:
            entries = SourceEntry.objects.filter(
                entry_text_html__icontains=options['match'])

        changed = 0
        for entry in entries.order_by('pk'):
            cleaned = clean_html(entry.entry_text_html,
                                 join_lines=not options['keep_paragraphs'])
            if cleaned == entry.entry_text_html:
                continue
            changed += 1
            self.stdout.write(self.style.WARNING(f'\n=== SourceEntry {entry.pk} ==='))
            self.stdout.write('--- before ---')
            self.stdout.write(entry.entry_text_html)
            self.stdout.write('--- after ---')
            self.stdout.write(cleaned)
            if options['apply']:
                entry.entry_text_html = cleaned
                entry.save(update_fields=['entry_text_html'])

        if options['apply']:
            self.stdout.write(self.style.SUCCESS(f'\nUpdated {changed} entries.'))
        else:
            self.stdout.write(self.style.SUCCESS(
                f'\nDry run: {changed} entries would change. Re-run with --apply.'))
