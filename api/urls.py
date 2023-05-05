from django.urls import path

from . import api_view

urlpatterns = [
    path('filter_selector', api_view.filter_selector, name='filter_selector'),
]
