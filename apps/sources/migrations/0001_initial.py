# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrimarySource',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(blank=True, null=True, max_length=128)),
                ('pvma_call_num', models.CharField(blank=True, null=True, max_length=32)),
                ('description', models.TextField(blank=True, null=True)),
                ('year_start', models.IntegerField(default=0, verbose_name='Start year or single')),
                ('year_end', models.IntegerField(default=0, verbose_name='End year if range')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SourceCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(blank=True, null=True, max_length=128)),
                ('sec_person_id', models.CharField(blank=True, null=True, max_length=32)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SourceEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('entry_text', models.CharField(max_length=255)),
                ('clarified', models.CharField(blank=True, null=True, max_length=255)),
                ('aa_id', models.IntegerField(default=0, verbose_name='aa id if known for sure')),
                ('secondary_person_id', models.IntegerField(default=0, verbose_name='2ndary person ID, only if aa id not known')),
                ('name_note', models.CharField(blank=True, null=True, max_length=64, verbose_name='Name note if no id known')),
                ('primary_source', models.ForeignKey(to='sources.PrimarySource', on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='primarysource',
            name='source_collection',
            field=models.ForeignKey(to='sources.SourceCollection', on_delete=models.CASCADE),
            preserve_default=True,
        ),
    ]
