from .views import BukuViewset, AnggotaViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'buku', BukuViewset, basename='buku')
router.register(r'anggota', AnggotaViewset, basename='anggota')

urlpatterns = router.urls