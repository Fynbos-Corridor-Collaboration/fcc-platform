# Generated by Django 3.2 on 2021-05-28 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_page_content_html'),
    ]

    operations = [
        migrations.AddField(
            model_name='redlist',
            name='css',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
