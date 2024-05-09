from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import RakBuku, Penerbit, Pengarang, Buku
from .serializers import RakBukuSerializer, PenerbitSerializer, PengarangSerializer, BukuSerializer

class RakBukuList(APIView):
    """
    
    """
    def get(self, request, format=None):
        rak_buku = RakBuku.objects.all()
        serializer = RakBukuSerializer(rak_buku, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RakBukuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RakBukuDetail(APIView):
    """
    
    """
    def get_object(self, pk):
        try:
            return RakBuku.objects.get(pk=pk)
        except RakBuku.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        rak_buku = self.get_object(pk)
        serializer = RakBukuSerializer(rak_buku)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        rak_buku = self.get_object(pk)
        serializer = RakBukuSerializer(rak_buku, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        rak_buku = self.get_object(pk)
        rak_buku.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PenerbitList(APIView):
    """
     penerbit,
    """
    def get(self, request, format=None):
        penerbit = Penerbit.objects.all()
        serializer = PenerbitSerializer(penerbit, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PenerbitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PenerbitDetail(APIView):
    """

    """
    def get_object(self, pk):
        try:
            return Penerbit.objects.get(pk=pk)
        except Penerbit.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        penerbit = self.get_object(pk)
        serializer = PenerbitSerializer(penerbit)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        penerbit = self.get_object(pk)
        serializer = PenerbitSerializer(penerbit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        penerbit = self.get_object(pk)
        penerbit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PengarangList(APIView):
    """

    """
    def get(self, request, format=None):
        pengarang = Pengarang.objects.all()
        serializer = PengarangSerializer(pengarang, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PengarangSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PengarangDetail(APIView):
    """

    """
    def get_object(self, pk):
        try:
            return Pengarang.objects.get(pk=pk)
        except Pengarang.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        pengarang = self.get_object(pk)
        serializer = PengarangSerializer(pengarang)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        pengarang = self.get_object(pk)
        serializer = PengarangSerializer(pengarang, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pengarang = self.get_object(pk)
        pengarang.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BukuList(APIView):
    """

    """
    def get(self, request, format=None):
        buku = Buku.objects.all()
        serializer = BukuSerializer(buku, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BukuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BukuDetail(APIView):
    """

    """
    def get_object(self, pk):
        try:
            return Buku.objects.get(pk=pk)
        except Buku.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        buku = self.get_object(pk)
        serializer = BukuSerializer(buku)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        buku = self.get_object(pk)
        serializer = BukuSerializer(buku, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        buku = self.get_object(pk)
        buku.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
