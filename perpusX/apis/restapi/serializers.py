from rest_framework import serializers
from ..models import *

cover = serializers.ImageField(required=False)

class BukuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buku
        fields = ('bukuId','judul','penulis', 'penerbit', 'rak', 'cover', 'jumlah')


class AnggotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anggota
        fields = ('anggotaId','nama','alamat', 'nomor_telepon', 'fakultas', 'email')