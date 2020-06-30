from django.shortcuts import render
from django.http import HttpResponse
from .models import TaxRateEstimation

# Create your views here.

def index(request):
    return render(request,'wacc_calculator/index.html', {"name": "Keil"})

def calculate_wacc(request):
    income_before_tax = int(request.GET['ibt'])
    income_tax_expenses = int(request.GET['itx'])
    interest_expenses = int(request.GET['ie'])
    short_current_lt_debt = int(request.GET['scltd'])
    lt_debt = int(request.GET['ltd'])
    rf_rate = float(request.GET['rf'])
    beta = float(request.GET['cb'])
    market_return = float(request.GET['mr'])
    total_debt = int(request.GET['td'])
    market_cap = int(request.GET['mc'])

    tax_rate = round(income_tax_expenses/income_before_tax, 2)
    cost_of_debt = round(interest_expenses/(short_current_lt_debt + lt_debt), 2)
    capm = round(rf_rate + beta*(market_return - rf_rate), 2)
    debt_weight = round(total_debt / (total_debt + market_cap), 2)
    equity_weight = round(market_cap / (total_debt + market_cap), 2)

    wacc_value = debt_weight * cost_of_debt * (1 - tax_rate) + equity_weight * capm

    context = {'tax_rate': tax_rate,
               'cost_of_debt': cost_of_debt,
               'capm': capm,
               'debt_weight':debt_weight,
               'equity_weight': equity_weight,
               'wacc_value': wacc_value
               }

    return render(request, 'wacc_calculator/results.html', context=context)

