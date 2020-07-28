from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('pl/', views.indexPL),
    path('ch/', views.indexCH),
    path('ar/', views.indexAR),
]