from django.views.generic import TemplateView
from django.shortcuts import render

def stroop(request):
    return render(request, 'stroop.html', {'zgodne': {'zielony': 'green', 'niebieski' : 'blue'},
                                           'niezgodne': {'czerwone':'blue', 'pstrokaty':'yellow'}})

class HomePageView(TemplateView):
    template_name = 'home.html'

class SettingsPageView(TemplateView):
    template_name = 'settings.html'
