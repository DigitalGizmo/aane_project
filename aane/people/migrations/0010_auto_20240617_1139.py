# Generated by Django 3.2.18 on 2024-06-17 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0009_auto_20231108_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='aaperson',
            name='research_status',
            field=models.IntegerField(choices=[(0, 'delete'), (1, 'inactive'), (2, 'research'), (3, 'problematic'), (4, 'approved')], default=0),
        ),
        migrations.AddField(
            model_name='operson',
            name='research_status',
            field=models.IntegerField(choices=[(0, 'delete'), (1, 'inactive'), (2, 'research'), (3, 'problematic'), (4, 'approved')], default=0),
        ),
    ]