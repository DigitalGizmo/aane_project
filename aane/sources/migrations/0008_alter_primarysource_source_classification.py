# Generated by Django 3.2.3 on 2022-04-19 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0007_auto_20220416_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primarysource',
            name='source_classification',
            field=models.CharField(choices=[('primary', 'primary'), ('secondary', 'secondary')], max_length=32, verbose_name='Classification'),
        ),
    ]