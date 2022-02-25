from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='supplychain_welcome'),
]

