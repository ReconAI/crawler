# Generated by Django 3.0.6 on 2020-05-31 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_search', '0005_videosearchresult_published_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='videosearchresult',
            name='duration',
            field=models.IntegerField(help_text='Video duration', null=True),
        ),
        migrations.AddField(
            model_name='videosearchresult',
            name='height',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='videosearchresult',
            name='width',
            field=models.IntegerField(null=True),
        ),
    ]
