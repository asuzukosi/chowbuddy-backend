from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from community.serializers import CommunitySerializer, PostSerializer, PostSerializerDetailed
from community.models import Community, Post
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response

class CommunityViewSet(ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    
    
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializerDetailed
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = ["community"]
    ordering_fields = ["community"]
    search_fields = ["community"]

    
    def create(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post = serializer.save()
        serializer = PostSerializerDetailed(post)
        return Response(serializer.data, 201)
