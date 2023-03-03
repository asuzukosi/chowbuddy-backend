from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from community.serializers import CommunitySerializer, PostSerializer
from community.models import Community, Post

class CommunityViewSet(ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    
    
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

