# Generated by Django 3.2 on 2021-05-28 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_vegetationtype_reference_spaces'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vegetationtype',
            old_name='reference_spaces',
            new_name='spaces',
        ),
    ]
