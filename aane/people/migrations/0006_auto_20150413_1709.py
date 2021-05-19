# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_auto_20150410_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='aaperson',
            name='alt_name_spelling',
            field=models.CharField(default='', max_length=32, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aaperson',
            name='freed_status',
            field=models.IntegerField(default=0, choices=[(1, 'enslaved'), (2, 'transition'), (3, 'always free')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aaperson',
            name='known_status',
            field=models.IntegerField(default=0, choices=[(1, 'known'), (2, 'owner known'), (3, 'unknown'), (9, 'discard')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aaperson',
            name='first_appearance_year',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aaperson',
            name='free_start_year',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aaperson',
            name='last_appearance_year',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aaperson',
            name='owner_id',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
