from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from .models import Buku
from .serializers import BukuSerializer


class BukuView(APIView):

    def post(self, request):
        data = request.data
        serializer = BukuSerializer(data=data)


        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Books Added Successfully", safe=False)
        return JsonResponse("Failed To added Books", safe=False)

    def get_buku(self, pk):
        try:
            buku = Buku.objects.get(bukuId=pk)
            return buku
        except Buku.DoesNotExist:
            raise Http404
        
    def get(self, request, pk=None):
        if pk:
            data = self.get_buku(pk)
            serializer = BukuSerializer(data)
        else:
            data = Buku.objects.all()
            serializer = BukuSerializer(data, many=True)
        return Response(serializer.data)
        