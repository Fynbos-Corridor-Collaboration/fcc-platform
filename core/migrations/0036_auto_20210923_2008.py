# Generated by Django 3.2.5 on 2021-09-23 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_auto_20210611_1303'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['position', 'date']},
        ),
        migrations.AddField(
            model_name='document',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
