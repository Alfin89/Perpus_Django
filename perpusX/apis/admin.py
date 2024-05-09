from django.contrib import admin
from .models import RakBuku, Penerbit, Pengarang, Buku

admin.site.register(RakBuku)
admin.site.register(Penerbit)
admin.site.register(Pengarang)
admin.site.register(Buku)
