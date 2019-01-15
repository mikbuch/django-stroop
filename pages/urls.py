from django.urls import path
from .views import HomePageView, experiment

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('experiment', experiment, name='experiment'),
]
