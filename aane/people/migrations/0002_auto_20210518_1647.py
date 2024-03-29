# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-05-18 20:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_squashed_0010_aaperson_freed_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aaperson',
            options={'ordering': ['known_status', 'freed_status', 'name'], 'verbose_name': 'African American'},
        ),
        migrations.AlterField(
            model_name='aaperson',
            name='known_status',
            field=models.IntegerField(choices=[(1, 'known'), (2, 'only ownr'), (3, 'unknown'), (9, 'discard')], default=0),
        ),
        migrations.AlterField(
            model_name='aaperson',
            name='owners',
            field=models.ManyToManyField(blank=True, to='people.OPerson', verbose_name='Owner(s)'),
        ),
    ]
