# Generated by Django 3.2.5 on 2021-07-15 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='url',
            field=models.URLField(default='', max_length=500),
        ),
    ]
