from django.db import models

# Create your models here.
class Anggota(models.Model):
    nama = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    nomor_telepon = models.CharField(max_length=255)
    fakultas = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.nama