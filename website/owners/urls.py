from django.urls import path

from . import views


app_name = 'owners'

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:owner_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:owner_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:owner_id>/vote/", views.vote, name="vote"),
]