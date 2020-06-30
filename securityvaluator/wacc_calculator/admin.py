from django.contrib import admin

from .models import TaxRateEstimation, CostOfDebtEstimation, CostOfEquityEstimation, Weights

# Register your models here.

admin.site.register(TaxRateEstimation)
admin.site.register(CostOfDebtEstimation)
admin.site.register(CostOfEquityEstimation)
admin.site.register(Weights)


