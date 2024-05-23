from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.my_view1),
    path('new_link/', views.my_view2),
    path('my_day/', views.my_view3)
]
