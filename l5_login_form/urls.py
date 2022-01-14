"""Login Form level app URL config"""

from django.urls import path

from .views import LoginView, ProfileView, LogoutView

app_name = "auth"

urlpatterns = [
    path("iniciar-sesion/", LoginView.as_view(), name="login"),
    path("perfil/", ProfileView.as_view(), name="profile"),
    path("cerrar-sesion/", LogoutView.as_view(), name="logout"),
]
