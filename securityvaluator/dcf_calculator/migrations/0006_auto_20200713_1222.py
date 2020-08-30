# Generated by Django 3.0.7 on 2020-07-13 10:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcf_calculator', '0005_auto_20200709_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterprise',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 13, 12, 22, 43, 571847)),
        ),
        migrations.AlterField(
            model_name='enterprise',
            name='fair_equity_value',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='enterprise',
            name='sector',
            field=models.CharField(default='all', max_length=400),
        ),
        migrations.AlterField(
            model_name='enterprise',
            name='stock_ticker',
            field=models.CharField(max_length=200),
        ),
    ]
