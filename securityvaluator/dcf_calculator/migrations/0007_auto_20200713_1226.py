# Generated by Django 3.0.7 on 2020-07-13 10:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcf_calculator', '0006_auto_20200713_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterprise',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 13, 12, 26, 42, 629625)),
        ),
        migrations.AlterField(
            model_name='enterprise',
            name='terminal_value',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='enterprise',
            name='todays_value',
            field=models.FloatField(null=True),
        ),
    ]
