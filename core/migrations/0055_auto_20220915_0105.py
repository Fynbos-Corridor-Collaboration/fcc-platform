# Generated by Django 3.2.8 on 2022-09-15 01:05

from django.db import migrations, models
import stdimage.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0054_auto_20211027_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='garden',
            name='uuid',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='corridor',
            name='image',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to='corridors', variations={'large': (1280, 1024), 'medium': (800, 600), 'thumbnail': (350, 350)}),
        ),
        migrations.AlterField(
            model_name='organization',
            name='logo',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to='pages', variations={'large': (1280, 1024), 'medium': (800, 600), 'thumbnail': (350, 350)}),
        ),
        migrations.AlterField(
            model_name='page',
            name='image',
            field=stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to='pages', variations={'large': (1280, 1024), 'medium': (800, 600), 'thumbnail': (350, 350)}),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to='photos', variations={'large': (1280, 1024), 'medium': (800, 600), 'thumbnail': (350, 350)}),
        ),
    ]
