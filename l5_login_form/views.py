"""Login Form level app views"""

from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class LoginView(auth_views.LoginView):
    """A view for sign in"""
    template_name = "l5_login_form/login.html"
    next_page = reverse_lazy("auth:profile")


class ProfileView(LoginRequiredMixin, TemplateView):
    """Shows profile view"""
    template_name = "l5_login_form/profile.html"


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout a user"""
    next_page = reverse_lazy("auth:login")
