from django.urls import path
from . import views

urlpatterns = [
    path('api/mma_news/', views.mma_news_list), # News
]
