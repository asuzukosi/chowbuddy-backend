from rest_framework.serializers import ModelSerializer
from customer.models import Customer, Friendship


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        

class FriendshipSerializer(ModelSerializer):
    class Meta:
        model = Friendship
        fields = '__all__'

