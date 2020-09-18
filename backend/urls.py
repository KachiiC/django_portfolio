from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.backend_home, name='backend-home'),
    path('post_list/', views.api_post_list, name='backend-post-list'),
    path('post_detail/<int:pk>', views.api_post_detail, name='backend-post-detail')
]