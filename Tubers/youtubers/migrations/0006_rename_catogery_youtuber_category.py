# Generated by Django 3.2.5 on 2021-09-11 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0005_rename_subs_countnt_youtuber_subs_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='youtuber',
            old_name='catogery',
            new_name='category',
        ),
    ]
