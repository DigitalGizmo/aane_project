# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AAPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('first_name', models.CharField(max_length=32, blank=True, null=True)),
                ('last_name', models.CharField(max_length=32, blank=True, null=True)),
                ('gender', models.CharField(max_length=12, choices=[('male', 'male'), ('female', 'female'), ('unknown', 'unknown')])),
                ('bio', models.TextField(blank=True, null=True)),
                ('birth_year', models.IntegerField(default=0)),
                ('death_year', models.IntegerField(default=0)),
                ('enslaved_start_year', models.IntegerField(default=0)),
                ('free_start_year', models.IntegerField(default=0)),
                ('owner_id', models.IntegerField(default=0)),
                ('place_of_origin', models.CharField(max_length=64, blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
