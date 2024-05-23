from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.shop_home),
    path('product/<int:product_id>/', views.shop_product),
    # path('/', views.),
    # re_path(r'profile/(?P<username>[\w]+)/$', views.profile),
]