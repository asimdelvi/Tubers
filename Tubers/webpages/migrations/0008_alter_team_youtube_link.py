# Generated by Django 3.2.5 on 2021-07-17 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0007_team_youtube_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='youtube_link',
            field=models.URLField(max_length=255),
        ),
    ]
