from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from customer.models import Customer
from customer.serializers import CustomerSerializer, RegisterCustomerSerializer
from rest_framework.response import Response

# Create your views here.
class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = RegisterCustomerSerializer(data=request.data)
        serializer.is_valid(raise_exceptions=True)
        customer = Customer.objects.create(**serializer.data)
        serializer = CustomerSerializer(instance=customer)
        return Response(serializer.data, 201)

