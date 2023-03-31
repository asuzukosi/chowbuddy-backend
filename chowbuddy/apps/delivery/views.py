from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from delivery.serializers import DelivererSerializer, DeliverySerializer, RegisterDelivererSerializer, UpdateDelivererLocationSerializer
from delivery.models import Deliverer, Delivery
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.
class DelivererViewSet(ModelViewSet):
    queryset = Deliverer.objects.all()
    serializer_class = DelivererSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = RegisterDelivererSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        deliverer = Deliverer.objects.create(**serializer.data)
        serializer = DelivererSerializer(instance=deliverer)
        return Response(serializer.data, 201)
    
    @action(methods=["post"], detail=True)
    def update_longlat(self, request, id, *args, **kwargs):
        deliverer = Deliverer.objects.get(id=id)
        serializer = UpdateDelivererLocationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        deliverer.setLongLat(**serializer.data)
        return Response({"message": "success"}, 200)
    
    
    
class DeliveryViewSet(ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    
    @action(methods=["get"], detail=True)
    def complete(self, request, id, *args, **kwargs):
        delivery:Delivery = Delivery.objects.get(id=id)
        delivery.complete()
        return Response({"message": "success"}, 200)


