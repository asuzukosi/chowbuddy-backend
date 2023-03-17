from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status 
from rest_framework import viewsets
from authentication.models import CustomUser
from authentication.serializers import CustomerTokenObtainPairSerializer, RestaurantTokenObtainPairSerializer, DelivererTokenObtainPairSerializer, CustomBaseUserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# Create your views here.
class CustomerTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomerTokenObtainPairSerializer
    
    
class RestaurantTokenObtainPairView(TokenObtainPairView):
    serializer_class = RestaurantTokenObtainPairSerializer
    
    
class DelivererTokenObtainPairView(TokenObtainPairView):
    serializer_class = DelivererTokenObtainPairSerializer
    
class CustomBaseUserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CustomBaseUserSerializer
    queryset = CustomUser.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = ["username", "email"]
    ordering_fields = ["email", "username"]
    search_fields = ["username", "email"]