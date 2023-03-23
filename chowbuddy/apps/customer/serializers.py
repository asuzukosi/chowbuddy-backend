from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from customer.models import Customer


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        


class RegisterCustomerSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    phone_number = serializers.CharField()
    address = serializers.CharField()

