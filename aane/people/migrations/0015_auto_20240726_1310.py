# Generated by Django 3.2.18 on 2024-07-26 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0014_auto_20240711_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='aaperson',
            name='confidence',
            field=models.IntegerField(blank=True, choices=[(1, 'confirmed identity'), (2, 'only enslaver known'), (3, 'indeterminate'), (4, 'possible duplicate')], null=True, verbose_name='Confidence Level'),
        ),
        migrations.AlterField(
            model_name='aaperson',
            name='freed_status',
            field=models.IntegerField(choices=[(1, 'enslaved'), (2, 'enslaved, then free'), (3, 'always free'), (4, 'unknown')], default=0),
        ),
        migrations.AlterField(
            model_name='aaperson',
            name='is_birth_circa',
            field=models.BooleanField(default=False, verbose_name='circa'),
        ),
        migrations.AlterField(
            model_name='aaperson',
            name='is_death_circa',
            field=models.BooleanField(default=False, verbose_name='circa'),
        ),
        migrations.AlterField(
            model_name='aaperson',
            name='owners',
            field=models.ManyToManyField(blank=True, to='people.OPerson', verbose_name='Enslaver(s)'),
        ),
        migrations.AlterField(
            model_name='operson',
            name='is_birth_circa',
            field=models.BooleanField(default=False, verbose_name='circa'),
        ),
        migrations.AlterField(
            model_name='operson',
            name='is_death_circa',
            field=models.BooleanField(default=False, verbose_name='circa'),
        ),
    ]
