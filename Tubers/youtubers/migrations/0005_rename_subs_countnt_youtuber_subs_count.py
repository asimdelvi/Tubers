# Generated by Django 3.2.5 on 2021-07-18 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0004_alter_youtuber_height'),
    ]

    operations = [
        migrations.RenameField(
            model_name='youtuber',
            old_name='subs_countnt',
            new_name='subs_count',
        ),
    ]