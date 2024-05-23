from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.viceversa_home),
    path('reversed/', views.reversed, name='reverse'),
    # path('')
    # path('/', views.),
    # re_path(r'profile/(?P<username>[\w]+)/$', views.profile),
]