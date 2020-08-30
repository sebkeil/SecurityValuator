# Generated by Django 3.0.7 on 2020-07-15 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wacc_calculator', '0002_auto_20200625_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnterpriseWACC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income_before_tax', models.IntegerField()),
                ('income_tax_expenses', models.IntegerField()),
                ('interest_expenses', models.IntegerField()),
                ('short_current_lt_debt', models.IntegerField()),
                ('lt_debt', models.IntegerField()),
                ('rf_rate', models.FloatField()),
                ('beta', models.FloatField()),
                ('market_return', models.FloatField()),
                ('total_debt', models.IntegerField()),
                ('market_cap', models.IntegerField()),
                ('tax_rate', models.FloatField()),
                ('cost_of_debt', models.FloatField()),
                ('capm', models.FloatField()),
                ('debt_weight', models.FloatField()),
                ('equity_weight', models.FloatField()),
                ('wacc_value', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='CostOfDebtEstimation',
        ),
        migrations.DeleteModel(
            name='CostOfEquityEstimation',
        ),
        migrations.DeleteModel(
            name='TaxRateEstimation',
        ),
        migrations.DeleteModel(
            name='Weights',
        ),
    ]
