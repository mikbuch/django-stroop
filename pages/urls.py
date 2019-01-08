from django.urls import path
from .views import HomePageView, SettingsPageView, stroop

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('settings/', SettingsPageView.as_view(), name='settings'),
    path('stroop/', stroop, name='stroop')
]
