# Generated by Django 3.0.7 on 2020-07-15 09:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcf_calculator', '0010_auto_20200714_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterprise',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 15, 11, 51, 24, 467560)),
        ),
    ]