# Generated by Django 3.2.5 on 2021-08-16 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20210816_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiretuber',
            name='phone_number',
            field=models.IntegerField(blank=True),
        ),
    ]
