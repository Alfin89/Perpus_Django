from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Anggota
from .serializers import AnggotaSerializer

class AnggotaList(APIView):
   
    def get(self, request, format=None):
        anggota = Anggota.objects.all()
        serializer = AnggotaSerializer(anggota, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AnggotaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnggotaDetail(APIView):
  
    def get_object(self, pk):
        try:
            return Anggota.objects.get(pk=pk)
        except Anggota.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        anggota = self.get_object(pk)
        serializer = AnggotaSerializer(anggota)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        anggota = self.get_object(pk)
        serializer = AnggotaSerializer(anggota, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        anggota = self.get_object(pk)
        anggota.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
