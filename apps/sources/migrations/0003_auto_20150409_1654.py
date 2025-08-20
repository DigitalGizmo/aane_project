# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0002_auto_20150313_1211'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='primarysource',
            options={'ordering': ['pk'], 'verbose_name': 'Source'},
        ),
        migrations.RenameField(
            model_name='sourceentry',
            old_name='secondary_person_id',
            new_name='operson_id',
        ),
        migrations.RemoveField(
            model_name='primarysource',
            name='pvma_call_num',
        ),
        migrations.RemoveField(
            model_name='primarysource',
            name='source_collection',
        ),
        migrations.RemoveField(
            model_name='sourcecollection',
            name='sec_person_id',
        ),
        migrations.AddField(
            model_name='primarysource',
            name='operson_id',
            field=models.IntegerField(default=0, verbose_name='O Person id if known'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='primarysource',
            name='pub_info',
            field=models.CharField(max_length=128, default='', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='primarysource',
            name='source_type',
            field=models.CharField(max_length=32, default='', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sourceentry',
            name='date_range',
            field=models.CharField(blank=True, default='', max_length=32, verbose_name='Date range (from title field)'),
            preserve_default=True,
        ),
        # migrations.AddField(
        #     model_name='sourceentry',
        #     name='location',
        #     field=models.CharField(blank=True, default='', max_length=32, verbose_name='Other location info'),
        #     preserve_default=True,
        # ),
        migrations.AddField(
            model_name='sourceentry',
            name='page_num',
            field=models.CharField(blank=True, default='', max_length=32, verbose_name='Page info'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sourceentry',
            name='pvma_call_num',
            field=models.CharField(max_length=32, default='', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='primarysource',
            name='description',
            field=models.TextField(default='', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='primarysource',
            name='title',
            field=models.CharField(max_length=128, default='', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourcecollection',
            name='description',
            field=models.TextField(default='', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourcecollection',
            name='title',
            field=models.CharField(max_length=128, default='', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='clarified',
            field=models.CharField(max_length=255, default='', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='name_note',
            field=models.CharField(blank=True, default='', max_length=64, verbose_name='Name note if no id known'),
            preserve_default=True,
        ),
    ]
