from django.contrib import admin
from .models import Buku


models_list = [Buku]
admin.site.register(models_list)
