from django.urls import path
from .views import BukuView

urlpatterns = [
    path('buku/', BukuView.as_view()),
    path('buku/<int:pk>/', BukuView.as_view()),
]