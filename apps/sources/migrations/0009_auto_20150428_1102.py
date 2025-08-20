# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0008_auto_20150427_1618'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='sourceentry',
        #     name='location',
        # ),
        migrations.AddField(
            model_name='sourceentry',
            name='access_order',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sourceentry',
            name='dollars',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sourceentry',
            name='event',
            field=models.CharField(blank=True, default='', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sourceentry',
            name='farthing',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sourceentry',
            name='legacy_enslaved_id',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sourceentry',
            name='notes',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sourceentry',
            name='pence',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sourceentry',
            name='pounds',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sourceentry',
            name='shillings',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sourceentry',
            name='transaction_note',
            field=models.CharField(blank=True, default='', max_length=64),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sourceentry',
            name='upr_day',
            field=models.IntegerField(blank=True, verbose_name='Day of month (number)', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sourceentry',
            name='upr_month',
            field=models.IntegerField(blank=True, verbose_name='Month (number)', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sourceentry',
            name='vol_book',
            field=models.CharField(blank=True, default='', max_length=32, verbose_name='Volume or book info'),
            preserve_default=True,
        ),
    ]
