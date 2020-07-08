from django.shortcuts import render
from .forms import EnterpriseModelForm

from .models import Enterprise
# Create your views here.

def dcf_index(request):
    return render(request, 'dcf_calculator/dcf_index.html', context= {})

def make_dcf_calculations(request):
    total_cash_flows_operating_activities_sly = int(request.GET['tcfoa_sly'])
    total_cash_flows_operating_activities_ly = int(request.GET['tcfoa_ly'])
    capex_sly = int(request.GET['ce_sly'])
    capex_ly = int(request.GET['ce_ly'])
    fcf_sly = total_cash_flows_operating_activities_sly - capex_sly
    fcf_ly = total_cash_flows_operating_activities_ly - capex_ly

    revenue_sly = int(request.GET['rev_sly'])
    revenue_ly = int(request.GET['rev_ly'])
    interest_expenses_sly = int(request.GET['ie_sly'])
    interest_expenses_ly = int(request.GET['ie_ly'])
    income_before_tax_sly = int(request.GET['ibt_sly'])
    income_before_tax_ly = int(request.GET['ibt_ly'])
    net_income_sly = int(request.GET['ni_sly'])
    net_income_ly = int(request.GET['ni_ly'])
    net_profit_margins_sly = net_income_sly/revenue_sly
    net_profit_margins_ly = net_income_ly/revenue_ly
    fcf_profit_margins_sly = fcf_sly/net_income_sly
    fcf_profit_margins_ly = fcf_ly/net_income_ly

    # estimators needed for forecasting revenues and cash flows
    revenue_growth_rate = (revenue_ly - revenue_sly)/revenue_sly
    average_net_income_margins = (net_profit_margins_sly + net_profit_margins_ly)/2
    average_fcf_income_margins = (fcf_profit_margins_sly + fcf_profit_margins_ly)/2

    #rate assumptions
    wacc = float(request.GET['wacc'])
    perpetual_growth_rate = float(request.GET['pgr'])
    shares_outstanding = int(request.GET['so'])

    # project revenues
    revenue_projections = [revenue_sly, revenue_ly]
    while len(revenue_projections) <= 5:
        next_revenue = revenue_projections[-1] * (1 + revenue_growth_rate)
        revenue_projections.append(next_revenue)

    # project net income:
    i = 2
    net_income_projections = [net_income_sly, net_income_ly]
    while len(net_income_projections) <= 5:
        next_net_income = revenue_projections[i] * average_net_income_margins
        net_income_projections.append(next_net_income)
        i += 1

    # project free cash flows
    i = 2
    fcf_projections = [fcf_sly, fcf_ly]
    while len(fcf_projections) <= 5:
        next_fcf = net_income_projections[i] * average_fcf_income_margins
        fcf_projections.append(next_fcf)
        i += 1

    # calculation steps
    terminal_value = fcf_projections[-1] * (1+perpetual_growth_rate) / (wacc - perpetual_growth_rate)
    pv_future_cash_flows = []
    i = 1
    for cash_flow in fcf_projections[2:]:
        pv_cash_flow = cash_flow/(1+wacc)**i
        pv_future_cash_flows.append(pv_cash_flow)
        i += 1
    pv_future_cash_flows.append(terminal_value)
    todays_value = sum(pv_future_cash_flows)
    fair_equity_value = todays_value/shares_outstanding

    context = {
        'revenue_projections': revenue_projections,
        'net_income_projections': net_income_projections,
        'fcf_projections': fcf_projections,
        'fair_equity_value': fair_equity_value
    }

    """
    qs = Enterprise.objects.all().values()
    data = pd.DataFrame(qs)
    
    context = {'df': data.html()}
    
    # in template : {{ df | save }}
    
    """

    return render(request, 'dcf_calculator/dcf_results.html', context)


def create_enterprise_view(request):
    form = EnterpriseModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = EnterpriseModelForm()
    context = {
        'form': form
    }
    return render(request, 'dcf_calculator/create_enterprise.html', context)