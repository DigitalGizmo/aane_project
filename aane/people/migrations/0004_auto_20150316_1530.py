# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_auto_20150311_1512'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aaperson',
            old_name='enslaved_start_year',
            new_name='first_appearance_year',
        ),
        migrations.AddField(
            model_name='aaperson',
            name='last_appearance_year',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aaperson',
            name='owners',
            field=models.ManyToManyField(blank=True, to='people.OPerson', verbose_name='Owner(s)', null=True),
            preserve_default=True,
        ),
    ]
