# Generated by Django 3.2.18 on 2024-01-03 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0009_auto_20231108_1136'),
        ('sources', '0030_rename_aa_ids_sourceentry_aa_persons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sourceentry',
            name='aa_persons',
            field=models.ManyToManyField(blank=True, related_name='aa_persons', to='people.AAPerson'),
        ),
    ]
