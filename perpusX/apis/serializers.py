from rest_framework import serializers
from .models import Buku, Pengarang, Penerbit, RakBuku

class PengarangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengarang
        fields = '__all__'

class PenerbitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Penerbit
        fields = '__all__'

class RakBukuSerializer(serializers.ModelSerializer):
    class Meta:
        model = RakBuku
        fields = '__all__'

class BukuSerializer(serializers.ModelSerializer):
    penulis = PengarangSerializer()
    penerbit = PenerbitSerializer()
    rak = RakBukuSerializer()

    class Meta:
        model = Buku
        fields = '__all__'