from django.urls import path
from .views import HomePageView, experiment, pre_experiment

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('experiment', experiment, name='experiment'),
    path('pre_experiment', pre_experiment, name='pre_experiment')
]
