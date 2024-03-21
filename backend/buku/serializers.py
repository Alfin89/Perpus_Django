from rest_framework import serializers
from . models import Buku


cover = serializers.ImageField(required=False)

class BukuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buku
        fields = ('bukuId','kd_buku', 'judul_buku', 'pengarang', 'jenis_buku', 'penerbit', 'cover')