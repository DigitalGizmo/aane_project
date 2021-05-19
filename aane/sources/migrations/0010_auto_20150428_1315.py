# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0009_auto_20150428_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primarysource',
            name='description',
            field=models.TextField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='primarysource',
            name='pub_info',
            field=models.CharField(blank=True, max_length=128, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='primarysource',
            name='title',
            field=models.CharField(blank=True, max_length=128, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='clarified',
            field=models.CharField(blank=True, max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='date_note',
            field=models.CharField(blank=True, max_length=124, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='date_range',
            field=models.CharField(blank=True, verbose_name='Date range (from title field)', max_length=32, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='event',
            field=models.CharField(blank=True, max_length=128, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='name_note',
            field=models.CharField(blank=True, verbose_name='Name note if no id known', max_length=64, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='notes',
            field=models.CharField(blank=True, max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='page_num',
            field=models.CharField(blank=True, verbose_name='Page info', max_length=32, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='pvma_call_num',
            field=models.CharField(blank=True, max_length=32, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='transaction_note',
            field=models.CharField(blank=True, max_length=64, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='vol_book',
            field=models.CharField(blank=True, verbose_name='Volume or book info', max_length=32, null=True),
            preserve_default=True,
        ),
    ]
