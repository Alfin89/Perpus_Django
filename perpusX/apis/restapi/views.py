from ..models import Buku, Anggota
from .serializers import BukuSerializer, AnggotaSerializer
from rest_framework import viewsets, generics


class BukuViewset(viewsets.ModelViewSet):
    serializer_class = BukuSerializer
    queryset = Buku.objects.all()

class AnggotaViewset(viewsets.ModelViewSet):
    serializer_class = AnggotaSerializer
    queryset = Anggota.objects.all()