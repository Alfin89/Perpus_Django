from django.db import models

# Create your models here.
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Buku(models.Model):
    bukuId = models.AutoField(primary_key=True)
    kd_buku = models.CharField(max_length=10, unique=True)
    judul_buku = models.CharField(max_length=32)
    pengarang = models.CharField(max_length=32)
    jenis_buku = models.CharField(max_length=32)
    penerbit = models.CharField(max_length=32)
    cover = models.ImageField(upload_to=upload_to, blank=True, null=True)