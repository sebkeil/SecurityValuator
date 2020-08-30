from django.db import models
from django.utils.functional import cached_property

# Create your models here.
class EnterpriseWACC(models.Model):
    """ data generated by user"""

    income_before_tax = models.IntegerField()
    income_tax_expenses = models.IntegerField()
    interest_expenses = models.IntegerField()
    short_current_lt_debt = models.IntegerField()
    lt_debt = models.IntegerField()
    rf_rate = models.FloatField()
    beta = models.FloatField()
    market_return = models.FloatField()
    total_debt = models.IntegerField()
    market_cap = models.IntegerField()

    """data generated in the view"""

    tax_rate = models.FloatField()
    cost_of_debt = models.FloatField()
    capm = models.FloatField()
    debt_weight = models.FloatField()
    equity_weight = models.FloatField()

    # final result
    wacc_value = models.FloatField()

