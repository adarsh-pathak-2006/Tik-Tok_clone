from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('like/<int:video_id>/', views.like_video, name='like_video'),
]