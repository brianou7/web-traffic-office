from django.urls import path

from .views import AuthView, SignUpView, logout_view


app_name = 'auth'

urlpatterns = [
    path("", AuthView.as_view(), name="index"),
    path("sign-up", SignUpView.as_view(), name="sign-up"),
    path("logout", logout_view, name="logout")
]
