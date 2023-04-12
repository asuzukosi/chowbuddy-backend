from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from customer.models import Customer
from authentication.serializers import CustomBaseUserSerializer


class CustomerSerializer(ModelSerializer):
    user = CustomBaseUserSerializer()
    class Meta:
        model = Customer
        fields = '__all__'
        


class RegisterCustomerSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    address = serializers.CharField()

class UpdateCustomerLocationSerializer(serializers.Serializer):
    longitude = serializers.FloatField()
    latitude = serializers.FloatField()