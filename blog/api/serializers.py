from rest_framework import serializers


from blog import models


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = "__all__"


class PostImageSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.PostImage
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)
    post_image = PostImageSerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)
    class Meta:
        model = models.Post
        fields = "__all__"