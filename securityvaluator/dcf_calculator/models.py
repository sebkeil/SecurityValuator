from django.db import models
import datetime
# Create your models here.

class Enterprise(models.Model):
    """ data entered by the user """

    company_name = models.CharField(max_length=200)
    stock_ticker = models.CharField(max_length=200, default="all")
    sector = models.CharField(max_length=400)

    # cash flow statement information
    total_cash_flows_operating_activities_sly = models.IntegerField()
    total_cash_flows_operating_activities_ly = models.IntegerField()
    capex_sly = models.IntegerField()
    capex_ly = models.IntegerField()

    # income statement information
    revenue_sly = models.IntegerField()
    revenue_ly = models.IntegerField()
    net_income_sly = models.IntegerField()
    net_income_ly = models.IntegerField()

    # rate assumptions
    wacc = models.FloatField(default=0.085) # SP500 average
    perpetual_growth_rate = models.FloatField(default=0.025)
    shares_outstanding = models.IntegerField()

    """data generated in the view"""

    terminal_value = models.FloatField()
    todays_value = models.FloatField()
    fair_equity_value = models.FloatField()

    date_added = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.company_name

