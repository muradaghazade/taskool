# Generated by Django 3.2.3 on 2021-07-23 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210719_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='youtube_video_url',
            field=models.CharField(default='', max_length=1000, verbose_name='YouTube video url'),
            preserve_default=False,
        ),
    ]
