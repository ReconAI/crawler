# Generated by Django 3.0.6 on 2020-05-31 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video_search', '0002_videosearchresult_status'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='videoproject',
            table='apps_video_search__video_project',
        ),
        migrations.AlterModelTable(
            name='videosearchresult',
            table='apps_video_search__search_result',
        ),
    ]
