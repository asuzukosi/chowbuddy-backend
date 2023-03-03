from rest_framework.serializers import ModelSerializer
from delivery.models import Deliverer, Delivery

class DelivererSerializer(ModelSerializer):
    class Meta:
        model = Deliverer
        fields = '__all__'
        
class DeliverySerializer(ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'
