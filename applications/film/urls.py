from django.urls import path
from . import views

app_name = 'film'

urlpatterns = [
    path('see/<str:slug>', views.index, name='index'),
]
