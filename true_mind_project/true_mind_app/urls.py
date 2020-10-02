#Add URL maps to redirect the base URL to our application
from django.urls import path
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
    path('', views.home),
]
