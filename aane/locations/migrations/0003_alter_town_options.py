# Generated by Django 3.2.18 on 2023-05-24 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_town'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='town',
            options={'ordering': ['title']},
        ),
    ]
