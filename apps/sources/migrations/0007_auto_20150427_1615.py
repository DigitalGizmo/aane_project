# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0006_delete_sourcecollection'),
    ]

    operations = [
        migrations.AddField(
            model_name='sourceentry',
            name='date_note',
            field=models.CharField(blank=True, default='', max_length=124),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sourceentry',
            name='date_status',
            field=models.IntegerField(default=0, choices=[(0, 'As written'), (1, 'Before'), (2, 'After'), (3, 'Uncertain'), (4, 'Unknown')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sourceentry',
            name='original_id',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='year_end',
            field=models.IntegerField(blank=True, null=True, verbose_name='Upper year if range'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='year_start',
            field=models.IntegerField(blank=True, null=True, verbose_name='Lower year or single'),
            preserve_default=True,
        ),
    ]
