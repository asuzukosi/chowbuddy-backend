from rest_framework.serializers import ModelSerializer
from delivery.models import Deliverer, Delivery
from rest_framework import serializers

class DelivererSerializer(ModelSerializer):
    class Meta:
        model = Deliverer
        fields = '__all__'
        
class DeliverySerializer(ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'
        

class RegisterDelivererSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    location = serializers.CharField()
