from django.urls import path
from . import views

urlpatterns = [
    path('', views.windowConfig, name='system_info'),
]