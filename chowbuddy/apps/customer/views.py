from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from customer.models import Customer
from customer.serializers import CustomerSerializer, RegisterCustomerSerializer, UpdateCustomerLocationSerializer
from community.serializers import CommunitySerializer
from meal.serializers import MealPlanSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# Create your views here.
class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = ["user"]
    ordering_fields = ["user"]
    search_fields = ["user"]
    
    def create(self, request, *args, **kwargs):
        serializer = RegisterCustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        customer = Customer.objects.create(**serializer.data)
        serializer = CustomerSerializer(instance=customer)
        return Response(serializer.data, 201)
    
    @action(methods=["get"], detail=True)
    def my_communities(self, request, pk,  *args, **kwargs):
        user = get_user_model().objects.get(id=pk)
        customer:Customer = Customer.objects.get(user=user)
        communities = customer.getMyCommunities()
        serializer = CommunitySerializer(instance=communities, many=True)
        return Response(serializer.data, 200)
    
    @action(methods=["get"], detail=True)
    def suggested_communities(self, request, pk,  *args, **kwargs):
        user = get_user_model().objects.get(id=pk)
        customer:Customer = Customer.objects.get(user=user)
        communities = customer.getSuggestedCommunites()
        serializer = CommunitySerializer(instance=communities, many=True)
        return Response(serializer.data, 200)
    
    @action(methods=["post"], detail=True)
    def update_longlat(self, request, id, *args, **kwargs):
        customer:Customer = Customer.objects.get(id=id)
        serializer = UpdateCustomerLocationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        customer.setLongLat(**serializer.data)
        return Response({"message": "success"}, 200)
    
    @action(methods=["get"], detail=True)
    def get_all_my_meal_plans(self, request, id, *args, **kwargs):
        customer:Customer = Customer.objects.get(id=id)
        mealPlans = customer.getMealPlans()
        serializer = MealPlanSerializer(instance=mealPlans, many=True)
        return Response(serializer.data, 200)
        
        


