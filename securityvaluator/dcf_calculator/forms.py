from django import forms
from .models import Enterprise


class EnterpriseModelForm(forms.ModelForm):
    class Meta:
        model = Enterprise

        fields = [
            'company_name',
            'stock_ticker',
            'sector',
            'total_cash_flows_operating_activities_sly',
            'total_cash_flows_operating_activities_ly',
            'capex_sly',
            'capex_ly',
            'revenue_sly',
            'revenue_ly',
            'net_income_sly',
            'net_income_ly',
            'wacc',
            'perpetual_growth_rate',
            'shares_outstanding',
        ]

    def clean_company_name(self, *args, **kwargs):
        company_name = self.cleaned_data.get("company_name")
        if "BE" in company_name:
            return company_name
        else:
            raise forms.ValidationError("Your title needs to contain BE")



class RawEnterpriseForm(forms.Form):
    """ data entered by the user """

    company_name = forms.CharField(max_length=200)
    stock_ticker = forms.CharField(max_length=200)
    sector = forms.CharField(max_length=400, widget=forms.TextInput(attrs={"placeholder": "All Sectors"}))

    # cash flow statement information
    total_cash_flows_operating_activities_sly = forms.IntegerField()
    total_cash_flows_operating_activities_ly = forms.IntegerField()
    capex_sly = forms.IntegerField(label="CapEx", widget=forms.TextInput(attrs={"placeholder": "2018"}))
    capex_ly = forms.IntegerField(label="", widget=forms.TextInput(attrs={"placeholder": '2019'}))

    # income statement information
    revenue_sly = forms.IntegerField()
    revenue_ly = forms.IntegerField()
    net_income_sly = forms.IntegerField()
    net_income_ly = forms.IntegerField()

    # rate assumptions
    wacc = forms.FloatField(initial= 0.08)  # SP500 average
    perpetual_growth_rate = forms.FloatField(label='Peppet the Pepperpig', initial=0.025)
    shares_outstanding = forms.IntegerField()

    """data generated in the view"""

    terminal_value = forms.FloatField(required=False)
    todays_value = forms.FloatField(required=False)
    fair_equity_value = forms.FloatField(required=False)

