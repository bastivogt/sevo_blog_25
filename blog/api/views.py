from rest_framework import generics, mixins, status
from rest_framework.views import APIView
from rest_framework.response import Response

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
class CommentListCreateView(APIView):
    def get(self, request):
        comments = models.Comment.objects.all()
        serializer = serializers.CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = serializers.CommentSerializer(data=request.data)

        if serializer.is_valid():
            post = serializer.validated_data.get("post")
            if post.allow_comments:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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