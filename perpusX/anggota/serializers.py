from rest_framework import serializers
from .models import Anggota

class AnggotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anggota
        fields = ['id', 'nama', 'alamat', 'nomor_telepon', 'fakultas', 'email']
