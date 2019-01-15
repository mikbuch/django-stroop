from django.views.generic import TemplateView
from django.shortcuts import render

def experiment(request):
    return render(request, 'experiment.html', {'zgodne': {'zielony': 'green', 'niebieski' : 'blue'},
                                               'niezgodne': {'czerwone':'blue', 'pstrokaty':'yellow'}})

class HomePageView(TemplateView):
    template_name = 'home.html'
