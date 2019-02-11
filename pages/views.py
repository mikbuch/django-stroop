from django.views.generic import TemplateView
from django.shortcuts import render
import json


def experiment(request):

    parameters = {"zgodne": {"zielony": "green", "niebieski": "blue"},
                  "niezgodne": {"czerwone": "blue", "pstrokaty": "yellow"}}

    return render(request, 'experiment.html', {'parameters':
                                               json.dumps(parameters)})


class HomePageView(TemplateView):
    template_name = 'home.html'
