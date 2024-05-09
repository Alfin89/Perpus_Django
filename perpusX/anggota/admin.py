from django.contrib import admin
from .models import Anggota

@admin.register(Anggota)
class AnggotaAdmin(admin.ModelAdmin):
    list_display = ['nama', 'alamat', 'nomor_telepon', 'fakultas', 'email']
