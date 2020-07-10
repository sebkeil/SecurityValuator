from django import forms
from .models import Enterprise

class EnterpriseModelForm(forms.ModelForm):
    class Meta:
        model = Enterprise

        fields = [
            'company_name',
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
            'date_added'
        ]
