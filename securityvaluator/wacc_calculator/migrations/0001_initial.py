# Generated by Django 3.0.7 on 2020-06-22 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CostOfDebtEstimation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest_expenses', models.IntegerField()),
                ('short_current_lt_debt', models.IntegerField()),
                ('lt_debt', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CostOfEquityEstimation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rf_rate', models.FloatField(default=0.01)),
                ('beta', models.FloatField(default=1)),
                ('market_returns', models.FloatField(default=0.1)),
            ],
        ),
        migrations.CreateModel(
            name='TaxRateEstimation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income_before_tax', models.IntegerField()),
                ('income_tax_expenses', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Weights',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_debt', models.IntegerField()),
                ('market_cap', models.IntegerField()),
            ],
        ),
    ]
