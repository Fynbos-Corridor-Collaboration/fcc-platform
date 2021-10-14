# Generated by Django 3.2 on 2021-06-11 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_alter_species_features'),
    ]

    operations = [
        migrations.AddField(
            model_name='garden',
            name='active',
            field=models.BooleanField(db_index=True, default=True),
        ),
        migrations.AddField(
            model_name='garden',
            name='original',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='garden',
            name='phase_alienremoval',
            field=models.IntegerField(choices=[(1, 'In progress'), (2, 'Completed')], db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='garden',
            name='phase_assessment',
            field=models.IntegerField(choices=[(1, 'In progress'), (2, 'Completed')], db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='garden',
            name='phase_birdsinsects',
            field=models.IntegerField(choices=[(1, 'In progress'), (2, 'Completed')], db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='garden',
            name='phase_landscaping',
            field=models.IntegerField(choices=[(1, 'In progress'), (2, 'Completed')], db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='garden',
            name='phase_pioneers',
            field=models.IntegerField(choices=[(1, 'In progress'), (2, 'Completed')], db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='garden',
            name='phase_placemaking',
            field=models.IntegerField(choices=[(1, 'In progress'), (2, 'Completed')], db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='garden',
            name='phase_specialists',
            field=models.IntegerField(choices=[(1, 'In progress'), (2, 'Completed')], db_index=True, null=True),
        ),
    ]
