# Generated by Django 3.2.3 on 2022-04-19 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0010_sourceentry_volume'),
    ]

    operations = [
        migrations.AddField(
            model_name='primarysource',
            name='source_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='sources.sourcetype'),
        ),
    ]
