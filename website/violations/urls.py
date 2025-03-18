from django.urls import path

from .views import InfractionListView, ViolationListView, index


app_name = 'violations'

urlpatterns = [
    path('index', index, name='index'),
    path('', ViolationListView.as_view(), name='violations'),
    path('infractions', InfractionListView.as_view(), name='infractions'),
]