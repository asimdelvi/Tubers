# Generated by Django 3.2.5 on 2021-07-18 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0003_auto_20210717_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
    ]