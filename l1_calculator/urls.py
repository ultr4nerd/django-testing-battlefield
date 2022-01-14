"""Calculator level app URL config"""

from django.urls import path

from .views import CalculatorView

app_name = "calculator"

urlpatterns = [
    path("", CalculatorView.as_view(), name="calculator"),
]
