# Generated by Django 3.2.18 on 2024-05-16 15:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sources', '0033_auto_20240516_1131'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SourceEditHistory',
            new_name='SourceEntryEditHistory',
        ),
    ]
