# Generated by Django 3.2.5 on 2021-10-24 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0046_rename_g_photo_garden'),
    ]

    operations = [
        migrations.AddField(
            model_name='referencespace',
            name='meta_data',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
