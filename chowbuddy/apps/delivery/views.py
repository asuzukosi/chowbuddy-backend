from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from delivery.serializers import DelivererSerializer, DeliverySerializer
from delivery.models import Deliverer, Delivery

# Create your views here.
class DelivererViewSet(ModelViewSet):
    queryset = Deliverer.objects.all()
    serializer_class = DelivererSerializer
    
    
class DeliveryViewSet(ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer


