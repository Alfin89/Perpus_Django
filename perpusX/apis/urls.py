from django.urls import path
from .views import RakBukuList, RakBukuDetail, PenerbitList, PenerbitDetail, PengarangList, PengarangDetail, BukuList, BukuDetail

urlpatterns = [
    path('rakbuku/', RakBukuList.as_view(), name='rakbuku-list'),
    path('rakbuku/<int:pk>/', RakBukuDetail.as_view(), name='rakbuku-detail'),
    path('penerbit/', PenerbitList.as_view(), name='penerbit-list'),
    path('penerbit/<int:pk>/', PenerbitDetail.as_view(), name='penerbit-detail'),
    path('pengarang/', PengarangList.as_view(), name='pengarang-list'),
    path('pengarang/<int:pk>/', PengarangDetail.as_view(), name='pengarang-detail'),
    path('buku/', BukuList.as_view(), name='buku-list'),
    path('buku/<int:pk>/', BukuDetail.as_view(), name='buku-detail'),
]