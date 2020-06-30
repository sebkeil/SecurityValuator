from django.http import HttpResponse
from django.shortcuts import render

# define homepage views here

def mainpage(request):
    return render(request, 'mainpage.html', {})

