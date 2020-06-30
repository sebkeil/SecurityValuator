from django.db import models
from django.utils.functional import cached_property

# Create your models here.
class TaxRateEstimation(models.Model):
    income_before_tax = models.IntegerField()
    income_tax_expenses = models.IntegerField()

    @property
    def calculate_tax_rate(self):
        result = (self.income_tax_expenses / self.income_before_tax)
        if result < 0:
            return result * -1
        return result

class CostOfDebtEstimation(models.Model):
    interest_expenses = models.IntegerField()
    short_current_lt_debt = models.IntegerField()
    lt_debt = models.IntegerField()

    @property
    def calculate_cost_of_debt(self):
        result = self.interest_expenses / (self.short_current_lt_debt + self.lt_debt)
        if result < 0:
            return result
        return result


class CostOfEquityEstimation(models.Model):
    rf_rate = models.FloatField(default=0.01)
    beta = models.FloatField(default=1)
    market_return = models.FloatField(default=0.1)

    @property
    def calculate_capm(self):
        return self.rf_rate + self.beta * (self.market_return - self.rf_rate)


class Weights(models.Model):
    total_debt = models.IntegerField()
    market_cap = models.IntegerField()

    @property
    def debt_weight(self):
        return self.total_debt / (self.total_debt + self.market_cap)

    @property
    def equity_weight(self):
        return self.market_cap / (self.total_debt + self.market_cap)


class WACC:
    company_name = models.CharField
    wacc_id = models.IntegerField()

    #def calculate_wacc(self):
       # return self.equity_weight * self.calculate_capm + self.debt_weight * self.calculate_cost_of_debt * (1 - self.calculate_tax_rate)



