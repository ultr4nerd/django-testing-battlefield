"""Core views"""

from django.views.generic import TemplateView


class IndexView(TemplateView):
    """Shows index page"""
    template_name = "index.html"
