from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from delivery.serializers import DelivererSerializer, DeliverySerializer, RegisterDelivererSerializer
from delivery.models import Deliverer, Delivery
from rest_framework.response import Response

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
    
    
class DeliveryViewSet(ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer


