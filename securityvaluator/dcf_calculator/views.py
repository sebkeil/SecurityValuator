from django.shortcuts import render, get_object_or_404, redirect
from .forms import RawEnterpriseForm, EnterpriseModelForm
from .models import Enterprise

# Create your views here.

def dcf_index_view(request):
    return render(request, 'dcf_calculator/dcf_index.html', context={})


# using POST.get instead of GET
# sly= second last year; ly=last year
def dcf_results_view(request):

    company_name = request.POST.get('company_name')
    stock_ticker = request.POST.get('stock_ticker')
    sector = request.POST.get('sector')
    currency = request.POST.get('currency')

    total_cash_flows_operating_activities_sly = int(request.POST.get('tcfoa_sly'))
    total_cash_flows_operating_activities_ly = int(request.POST.get('tcfoa_ly'))
    capex_sly = int(request.POST.get('ce_sly'))
    capex_ly = int(request.POST.get('ce_ly'))
    fcf_sly = total_cash_flows_operating_activities_sly - capex_sly
    fcf_ly = total_cash_flows_operating_activities_ly - capex_ly

    revenue_sly = int(request.POST.get('rev_sly'))
    revenue_ly = int(request.POST.get('rev_ly'))
    #interest_expenses_sly = int(request.POST.get('ie_sly'))
    #interest_expenses_ly = int(request.POST.get('ie_ly'))
    #income_before_tax_sly = int(request.POST.get('ibt_sly'))
    #income_before_tax_ly = int(request.POST.get('ibt_ly'))
    net_income_sly = int(request.POST.get('ni_sly'))
    net_income_ly = int(request.POST.get('ni_ly'))
    net_profit_margins_sly = net_income_sly / revenue_sly
    net_profit_margins_ly = net_income_ly / revenue_ly
    fcf_profit_margins_sly = fcf_sly / net_income_sly
    fcf_profit_margins_ly = fcf_ly / net_income_ly

    # estimators needed for forecasting revenues and cash flows
    revenue_growth_rate = (revenue_ly - revenue_sly) / revenue_sly
    average_net_income_margins = (net_profit_margins_sly + net_profit_margins_ly) / 2
    average_fcf_income_margins = (fcf_profit_margins_sly + fcf_profit_margins_ly) / 2

    # rate assumptions
    wacc = float(request.POST.get('wacc'))
    perpetual_growth_rate = float(request.POST.get('pgr')) # this should be the growth rate of the economy
    shares_outstanding = int(request.POST.get('so'))

    # project revenues
    revenue_projections = [revenue_sly, revenue_ly]
    while len(revenue_projections) <= 5:
        next_revenue = int(revenue_projections[-1] * (1 + revenue_growth_rate))
        revenue_projections.append(next_revenue)

    # project net income:
    i = 2
    net_income_projections = [net_income_sly, net_income_ly]
    while len(net_income_projections) <= 5:
        next_net_income = int(revenue_projections[i] * average_net_income_margins)
        net_income_projections.append(next_net_income)
        i += 1

    # project free cash flows
    i = 2
    fcf_projections = [fcf_sly, fcf_ly]
    while len(fcf_projections) <= 5:
        next_fcf = int(net_income_projections[i] * average_fcf_income_margins)
        fcf_projections.append(next_fcf)
        i += 1

    # calculation steps
    terminal_value = fcf_projections[-1] * (1 + perpetual_growth_rate) / (wacc - perpetual_growth_rate)
    pv_future_cash_flows = []
    i = 1
    for cash_flow in fcf_projections[2:]:
        pv_cash_flow = cash_flow / (1 + wacc) ** i
        pv_future_cash_flows.append(pv_cash_flow)
        i += 1
    pv_future_cash_flows.append(terminal_value/ (1 + wacc) ** i)
    todays_value = sum(pv_future_cash_flows)
    fair_equity_value = round(todays_value / shares_outstanding, 2)

    projected_years = ['2018A', '2019A', '2020E', '2021E', '2022E', '2023E']

    revenue_dict = dict(zip(projected_years, revenue_projections))
    net_income_dict = dict(zip(projected_years, net_income_projections))
    fcf_dict = dict(zip(projected_years, fcf_projections))

    context = {
        'company_name': company_name,
        'stock_ticker': stock_ticker,
        'currency': currency,
        'revenue_dict': revenue_dict,
        'net_income_dict': net_income_dict,
        'fcf_dict': fcf_dict,
        'fair_equity_value': fair_equity_value,
        'projected_years': projected_years
    }

    Enterprise.objects.create(company_name=company_name, stock_ticker=stock_ticker, sector=sector, total_cash_flows_operating_activities_sly = total_cash_flows_operating_activities_sly, total_cash_flows_operating_activities_ly = total_cash_flows_operating_activities_ly, capex_sly = capex_sly, capex_ly = capex_ly, revenue_sly = revenue_sly, revenue_ly = revenue_ly, net_income_sly = net_income_sly, net_income_ly = net_income_ly, wacc = wacc, perpetual_growth_rate = perpetual_growth_rate, shares_outstanding = shares_outstanding, terminal_value = terminal_value, todays_value = todays_value, fair_equity_value = fair_equity_value)

    """
    qs = Enterprise.objects.all().values()
    data = pd.DataFrame(qs)

    context = {'df': data.html()}

    # in template : {{ df | save }}

    """

    return render(request, 'dcf_calculator/dcf_results.html', context)


def enterprise_database_view(request):
    queryset = Enterprise.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, 'dcf_calculator/enterprise_database.html', context=context)

def dynamic_lookup_view(request, id):
    obj = get_object_or_404(Enterprise, id=id)
    context = {
        "object":obj,
    }
    return render(request, 'dcf_calculator/enterprise_detail.html', context)

def individual_stock_view(request):
    return render(request, 'dcf_calculator/individual_stock.html', context={})

def enterprise_delete_view(request, id):
    obj = get_object_or_404(Enterprise, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "dcf_calculator/enterprise_delete.html", context)