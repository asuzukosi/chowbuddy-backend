from rest_framework.serializers import ModelSerializer
from delivery.models import Deliverer, Delivery
from rest_framework import serializers
from authentication.serializers import CustomBaseUserSerializer

class DelivererSerializer(ModelSerializer):
    user = CustomBaseUserSerializer()
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


class UpdateDelivererLocationSerializer(serializers.Serializer):
    longitude = serializers.FloatField()
    latitude = serializers.FloatField()
    
class GetNearestDelivererSerializer(serializers.Serializer):
    longitude = serializers.FloatField()
    latitude = serializers.FloatField()