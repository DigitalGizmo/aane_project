# Generated by Django 3.2.18 on 2024-06-17 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0012_auto_20240617_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='aaperson',
            name='note',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='operson',
            name='note',
            field=models.TextField(blank=True, default=''),
        ),
    ]
