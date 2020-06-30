from django.shortcuts import render
from .models import HelpTutorial


# Create your views here.

def main_help(request):
    obj = HelpTutorial.objects.get(id=1)
    """
    context = {
        'title': obj.title,
        'main_text': obj.main_text,
        'publishing_date': obj.publishing_date
    }"""
    context = {
        'object': obj,
    }
    return render(request, 'help_text/main_help.html', context)