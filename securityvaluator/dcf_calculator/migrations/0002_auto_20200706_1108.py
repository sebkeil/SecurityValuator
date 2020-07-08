# Generated by Django 3.0.7 on 2020-07-06 09:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcf_calculator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterprise',
            name='sector',
            field=models.CharField(default='all', max_length=200),
        ),
        migrations.AlterField(
            model_name='enterprise',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 6, 11, 8, 40, 345274)),
        ),
    ]
