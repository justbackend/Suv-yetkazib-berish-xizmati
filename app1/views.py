from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import filters
class SuvApiSet(ModelViewSet):
    queryset = Suv.objects.all()
    serializer_class = SuvSerializer

class MijozApiSet(ModelViewSet):
    queryset = Mijoz.objects.all()
    serializer_class = MijozSerializer
    # filter_backends = [filters.SearchFilter]
    #
    # def list(self, request, *args, **kwargs):
    #     qidiruv_sozi = request.query_param.get('name')
    #     if qidiruv_sozi is not None:
    #         queryset = Mijoz.objects.filter(ism__contains=qidiruv_sozi)


class BuyurtmaApi(APIView):
    def get(self, request):
        buyurtma = Buyurtma.objects.all()
        serializer = BuyurtmaSerializer(buyurtma, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BuyurtmaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "Buyurtma created successfullly"})
        return Response(serializer.errors)

class AdminApi(APIView):
    def get(self, request):
        admin = Admin.objects.all()
        serializer = AdminSerializer(admin, many=True)
        return Response(serializer.data)

class AdminApiOne(APIView):
    def get(self, request, pk):
        admin = Admin.objects.get(id=pk)
        serializer = AdminSerializer(admin)
        return Response(serializer.data)

class HaydovchiApi(APIView):
    def get(self, request):
        haydovchi = Haydovchi.objects.all()
        serializer = HaydovchiSerializer(haydovchi, many=True)
        return Response(serializer.data)

class HaydovchiApiOne(APIView):
    def get(self, request, pk):
        haydovchi = Haydovchi.objects.get(id=pk)
        serializer = HaydovchiSerializer(haydovchi)
        return Response(serializer.data)


