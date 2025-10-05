from rest_framework import generics

from blog.api import serializers
from blog import models

# Tag
class TagListView(generics.ListAPIView):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer

class TagRetrieveView(generics.RetrieveAPIView):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer


# PostImage
class PostImageListView(generics.ListAPIView):
    queryset = models.PostImage.objects.all()
    serializer_class = serializers.PostImageSerializer

class PostImageRetrieveView(generics.RetrieveAPIView):
    queryset = models.PostImage.objects.all()
    serializer_class = serializers.PostImageSerializer

# Comment
class CommentListCreateView(generics.ListCreateAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer

class CommentRetrieveView(generics.RetrieveAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer

# Post
class PostListView(generics.ListAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer

class PostRetrieveView(generics.RetrieveAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer