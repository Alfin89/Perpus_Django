from django.db import models


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)
# Create your models here.
class RakBuku(models.Model):
  nama = models.CharField(max_length=255)

  def __str__(self):
    return self.nama

class Penerbit(models.Model):
  nama = models.CharField(max_length=255)

  def __str__(self):
    return self.nama

class Pengarang(models.Model):
  nama = models.CharField(max_length=255)

  def __str__(self):
    return self.nama

class Anggota(models.Model):
  anggotaId = models.AutoField(primary_key=True)
  nama = models.CharField(max_length=255)
  alamat = models.CharField(max_length=255)
  nomor_telepon = models.CharField(max_length=255)
  fakultas = models.CharField(max_length=255)
  email = models.CharField(max_length=255)

  def __str__(self):
    return self.nama

class Buku(models.Model):
  bukuId = models.AutoField(primary_key=True)
  judul = models.CharField(max_length=255)
  penulis = models.ForeignKey(Pengarang, on_delete=models.CASCADE)
  penerbit = models.ForeignKey(Penerbit, on_delete=models.CASCADE)
  rak = models.ForeignKey(RakBuku, on_delete=models.CASCADE)
  cover = models.ImageField(upload_to=upload_to, blank=True, null=True)
  jumlah = models.IntegerField()

  def __str__(self):
    return self.judul