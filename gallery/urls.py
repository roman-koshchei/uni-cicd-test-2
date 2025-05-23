from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery_view, name='gallery'),
    path('image/<int:pk>/', views.image_detail, name='image_detail'),
]
