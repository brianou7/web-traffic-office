from django.urls import path

from .views import AuthView, logout_view


app_name = 'auth'

urlpatterns = [
    path("", AuthView.as_view(), name="index"),
    path("logout", logout_view, name="logout")
]
