from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('2024/', views.index_2024),
    path('name/', views.index_name)
]