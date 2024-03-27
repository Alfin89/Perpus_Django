from django.contrib import admin
from . models import *

# Register your models here.

class TbRakBukuAdmin(admin.ModelAdmin):
  list_display = ("nama",)
  list_display_links = ("nama",)
  search_fields = ("nama",)
  list_per_page = 5

class TbPenerbitAdmin(admin.ModelAdmin):
  list_display = ("nama",)
  list_display_links = ("nama",)
  search_fields = ("nama",)
  list_per_page = 5

class TbPengarangAdmin(admin.ModelAdmin):
  list_display = ("nama",)
  list_display_links = ("nama",)
  search_fields = ("nama",)
  list_per_page = 5

class TbAnggotaAdmin(admin.ModelAdmin):
  list_display = ("nama", "alamat", "nomor_telepon","fakultas", "email")
  list_display_links = ("nama",)
  search_fields = ("nama", "alamat", "nomor_telepon","fakultas", "email")
  list_per_page = 5

class TbBukuAdmin(admin.ModelAdmin):
  list_display = ("judul", "penulis", "penerbit", "rak","cover", "jumlah")
  list_display_links = ("judul",)
  search_fields = ("judul", "penulis__nama", "penerbit__nama","cover", "rak__nama")
  list_filter = ("penulis", "penerbit", "rak")
  list_per_page = 5

admin.site.register(RakBuku, TbRakBukuAdmin)
admin.site.register(Penerbit, TbPenerbitAdmin)
admin.site.register(Pengarang, TbPengarangAdmin)
admin.site.register(Anggota, TbAnggotaAdmin)
admin.site.register(Buku, TbBukuAdmin)
