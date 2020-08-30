from django.db import models
from django.urls import reverse
import datetime
# Create your models here.

class Enterprise(models.Model):
    """ data entered by the user """

    company_name = models.CharField(max_length=200)
    stock_ticker = models.CharField(max_length=200)
    sector = models.CharField(max_length=400, default="all")

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

    @property
    def revenue_projections(self):
        rev_proj = [self.revenue_sly, self.revenue_ly]
        while len(rev_proj) <= 5:
            next_revenue = int(rev_proj[-1] * (1 + rev_proj))
            rev_proj.append(next_revenue)
        return rev_proj

    terminal_value = models.FloatField(null=True)
    todays_value = models.FloatField(null=True)
    fair_equity_value = models.FloatField(null=True)

    date_added = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.company_name

    def get_absolute_url(self):
        return f"enterprise_database/{self.id}"

