from django.views.generic import TemplateView
from django.shortcuts import render
import json


def experiment(request):

    parameters = {"zgodne": [{"zielony": "green"}, {"niebieski": "blue"}, {"czerwony": "red"}, {"żółty": "yellow"}],
                  "niezgodne": [{"czerwony": "blue"}, {"niebieski": "yellow"}, {"żółty": "green"}, {"zielony": "red"}],
                  "kontrolne": [{"xxxxxx": "red"}, {"xxxxxx": "green"}, {"xxxxxx": "blue"}, {"xxxxxx": "yellow"}]}

    return render(request, 'experiment.html', {'parameters':
                                               json.dumps(parameters)})


class HomePageView(TemplateView):
    template_name = 'home.html'
