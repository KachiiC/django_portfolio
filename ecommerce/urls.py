from django.urls import path
from . import views

urlpatterns = [
    path('', views.ecommerce_home.as_view(), name='home'),
    path('cart/<slug>', views.add_to_cart, name='cart'),
    path('remove/<slug>', views.remove_from_cart, name='remove-cart'),

]