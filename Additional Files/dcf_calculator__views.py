
from securityvaluator.dcf_calculator.forms import RawEnterpriseForm, EnterpriseModelForm
from securityvaluator.dcf_calculator.models import Enterprise
from django.shortcuts import render, get_object_or_404

def form_based_dcf_index_view(request):
    form = RawEnterpriseForm()
    if request.method == "POST":
     form = RawEnterpriseForm(request.POST)
    if form.is_valid():
        Enterprise.objects.create(**form.cleaned_data)
    context = {
        'form': form
    }
    return render(request, 'dcf_calculator/form_based_dcf_index.html', context)


def form_based_dcf_index_view_2(request):
    form = EnterpriseModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = EnterpriseModelForm()
    context = {
        'form': form
    }
    return render(request, 'dcf_calculator/form_based_dcf_index_2.html', context)


def form_based_dcf_results_view(request, id):
    obj = get_object_or_404(Enterprise, id=id)
    context = {'object':obj}
    return render(request, 'dcf_calculator/form_based_dcf_results.html', context=context)
