from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from community.serializers import CommunitySerializer, PostSerializer
from community.models import Community, Post
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class CommunityViewSet(ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    
    
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = ["community"]
    ordering_fields = ["community"]
    search_fields = ["community"]

