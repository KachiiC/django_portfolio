from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_home, name='chat-home'),
    path('<str:room_name>/', views.chat_room, name='room')
]
