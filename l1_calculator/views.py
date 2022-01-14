"""Calculator level views"""

from django.views.generic import TemplateView

from .services import calculate


class CalculatorView(TemplateView):
    """Show a calculator via GET and calculates with POST"""
    template_name = "l1_calculator/calculator.html"

    def get_context_data(self, **kwargs):
        first_number = self.request.GET.get('first_number')
        operation = self.request.GET.get('operation')
        second_number = self.request.GET.get('second_number')

        context = super().get_context_data(**kwargs)
        context['result'] = calculate(first_number, operation, second_number)

        return context
