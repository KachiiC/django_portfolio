from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.backend_home, name='backend-home'),
    path('post_list/', views.api_post_list, name='post_list'),
    path('post_detail/', views.api_post_detail, name='post_detail')
]