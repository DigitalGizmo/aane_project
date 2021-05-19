# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0011_auto_20150428_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primarysource',
            name='description',
            field=models.TextField(blank=True, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='primarysource',
            name='pub_info',
            field=models.CharField(blank=True, max_length=128, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='primarysource',
            name='title',
            field=models.CharField(blank=True, max_length=128, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='clarified',
            field=models.CharField(blank=True, max_length=255, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='date_note',
            field=models.CharField(blank=True, max_length=124, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='date_range',
            field=models.CharField(blank=True, default='', max_length=32, verbose_name='Date range (from title field)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='event',
            field=models.CharField(blank=True, max_length=128, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='name_note',
            field=models.CharField(blank=True, default='', max_length=64, verbose_name='Name note if no id known'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='notes',
            field=models.CharField(blank=True, max_length=255, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='page_num',
            field=models.CharField(blank=True, default='', max_length=64, verbose_name='Page info'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='pvma_call_num',
            field=models.CharField(blank=True, max_length=32, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='transaction_note',
            field=models.CharField(blank=True, max_length=64, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='vol_book',
            field=models.CharField(blank=True, default='', max_length=32, verbose_name='Volume or book info'),
            preserve_default=True,
        ),
    ]
