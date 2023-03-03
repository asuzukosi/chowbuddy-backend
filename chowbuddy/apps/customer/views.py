from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from customer.models import Customer, Friendship
from customer.serializers import CustomerSerializer, FriendshipSerializer

# Create your views here.
class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
    
class FriendshipViewSet(ModelViewSet):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer
