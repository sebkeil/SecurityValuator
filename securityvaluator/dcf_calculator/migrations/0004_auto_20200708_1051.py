# Generated by Django 3.0.7 on 2020-07-08 08:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcf_calculator', '0003_auto_20200708_1033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enterprise',
            name='fair_value',
        ),
        migrations.AddField(
            model_name='enterprise',
            name='capex_ly',
            field=models.IntegerField(default=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enterprise',
            name='capex_sly',
            field=models.IntegerField(default=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enterprise',
            name='net_income_ly',
            field=models.IntegerField(default=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enterprise',
            name='net_income_sly',
            field=models.IntegerField(default=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enterprise',
            name='perpetual_growth_rate',
            field=models.FloatField(default=0.025),
        ),
        migrations.AddField(
            model_name='enterprise',
            name='revenue_ly',
            field=models.IntegerField(default=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enterprise',
            name='revenue_sly',
            field=models.IntegerField(default=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enterprise',
            name='shares_outstanding',
            field=models.IntegerField(default=10000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enterprise',
            name='total_cash_flows_operating_activities_ly',
            field=models.IntegerField(default=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enterprise',
            name='total_cash_flows_operating_activities_sly',
            field=models.IntegerField(default=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='enterprise',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 8, 10, 50, 48, 336887)),
        ),
    ]
