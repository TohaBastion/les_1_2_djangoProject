from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
    re_path(r'profile/(?P<username>[\w]+)/$', views.profile),
]
