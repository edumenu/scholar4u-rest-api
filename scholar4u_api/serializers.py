from rest_framework import serializers
from . import models


class PostSerializer(serializers.ModelSerializer):
    """Serializes post"""

    class Meta:
        model = models.Post
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    """Serializes comment"""

    class Meta:
        model = models.Comment
        fields = "__all__"