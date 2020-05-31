# Generated by Django 3.0.6 on 2020-05-31 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videosearchresult',
            name='status',
            field=models.CharField(choices=[('CONFIRMED', 'CONFIRMED'), ('DISCARDED', 'DISCARDED')], max_length=100, null=True),
        ),
    ]
