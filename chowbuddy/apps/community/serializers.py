from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from community.models import Community, Post
from authentication.serializers import CustomBaseUserSerializer

class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = '__all__'
        

class PostSerializer(serializers.ModelSerializer):
    # author = CustomBaseUserSerializer()
    class Meta:
        model = Post
        fields = '__all__'
        
class PostSerializerDetailed(serializers.ModelSerializer):
    author = CustomBaseUserSerializer()
    class Meta:
        model = Post
        fields = '__all__'