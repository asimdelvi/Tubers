# Generated by Django 3.2.5 on 2021-08-19 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0009_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='heading',
            field=models.CharField(default=False, max_length=50),
            preserve_default=False,
        ),
    ]
