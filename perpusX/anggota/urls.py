from django.urls import path
from .views import AnggotaList, AnggotaDetail

urlpatterns = [
    path('anggota/', AnggotaList.as_view(), name='anggota-list'),
    path('anggota/<int:pk>/', AnggotaDetail.as_view(), name='anggota-detail'),
]
