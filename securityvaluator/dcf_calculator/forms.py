from django import forms
from .models import Enterprise

class EnterpriseModelForm(forms.ModelForm):
    class Meta:
        model = Enterprise
        fields = [
            'enterprise_name',
            'sector',
            'description',
            'date_added',
            'fair_value'
        ]
