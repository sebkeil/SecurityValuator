from django.shortcuts import render
from .models import HelpTutorial


# Create your views here.

def main_help(request):
    tutorials = HelpTutorial.objects.all()
    """
    context = {
        'title': obj.title,
        'main_text': obj.main_text,
        'publishing_date': obj.publishing_date
    }"""
    context = {
        'tutorials': tutorials,
    }
    return render(request, 'help_text/main_help.html', context)