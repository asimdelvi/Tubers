# Generated by Django 3.2.5 on 2021-08-30 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0010_about_heading'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='about_contect',
            new_name='about_content',
        ),
    ]
